from flask import send_from_directory, abort, request
from flask_restful import Resource
from . import BASE_DIR
from pathlib import Path
from werkzeug.utils import secure_filename
import markdown

class FileResource(Resource):
    def get(self, path):
        """Returns a file from the specified path in the base directory."""
        file_path = self._get_safe_path(path)
        
        if not file_path.is_file():
            abort(404, description="File not found.")
        
        # Check if user wants to view the file (instead of download)
        view_mode = request.args.get('view', 'false').lower() == 'true'
        
        return send_from_directory(
            file_path.parent, 
            file_path.name, 
            as_attachment=not view_mode
        )

    def post(self, path):
        """Upload a file to the specified path. Expects 'file' in multipart/form-data."""
        uploaded_file = self._validate_file_upload()
        
        # Secure the filename and create safe directory path
        filename = secure_filename(uploaded_file.filename)
        directory_path = self._get_safe_path(path) if path else Path(BASE_DIR)
        
        # Check if directory exists
        if not directory_path.exists():
            abort(404, description=f"Directory '{path}' does not exist.")
        
        safe_file_path = directory_path / filename
        
        # Save file
        uploaded_file.save(str(safe_file_path))
        
        return {"message": f"File uploaded successfully to {path}/{filename}" if path else f"File uploaded successfully to {filename}"}

    def delete(self, path):
        """Delete a file at the specified path."""
        file_path = self._get_safe_path(path)
        
        if not file_path.is_file():
            abort(404, description="File not found.")
        
        file_path.unlink()
        return {"message":f"File removed successfully."}


    def _validate_file_upload(self):
        """Validates file upload request."""
        if 'file' not in request.files:
            abort(400, description="No file provided in request.")
        
        file = request.files['file']
        if not file.filename:
            abort(400, description="No file selected.")
        
        return file
    
    def _get_safe_path(self, *path_parts):
        """Creates a safe path within BASE_DIR to prevent directory traversal."""
        # Join path parts and resolve to prevent directory traversal
        full_path = Path(BASE_DIR).joinpath(*path_parts).resolve()
        
        # Ensure the path is within BASE_DIR
        if not str(full_path).startswith(str(Path(BASE_DIR).resolve())):
            abort(400, description="Invalid path.")
        
        return full_path

class FolderResource(Resource):
    def get(self, path=None):
        """Returns all files and folders in the specified directory."""
        folder_path = self._get_folder_path(path)
        
        if not folder_path.is_dir():
            abort(404, description="Folder not found.")
        
        items = self._list_directory_items(folder_path)
        readme_content = self._get_readme_content(folder_path)
        
        return {
            "folder": path or 'base',
            "items": items,
            "readme": readme_content
        }

    def post(self, path):
        """Creates a new folder at the specified path."""
        if not path:
            abort(400, description="Folder path is required.")
        
        folder_path = self._get_safe_path(path)
        
        try:
            folder_path.mkdir(parents=True, exist_ok=True)
            return {"message": f"Folder created at {path}"}
        except OSError as e:
            abort(500, description=f"Failed to create folder: {str(e)}")
    
    def _get_folder_path(self, path):
        """Gets the folder path, defaulting to BASE_DIR if path is empty or 'base'."""
        if not path or path.lower() == 'base':
            return Path(BASE_DIR)
        return self._get_safe_path(path)
    
    def _list_directory_items(self, folder_path):
        """Lists all items in a directory with their types."""
        items = []
        try:
            for item in folder_path.iterdir():
                if str(item.name).startswith('.'):
                    continue
                item_type = "folder" if item.is_dir() else "file"
                item_size = f"{self._bytes_to_megabytes(item.stat().st_size):.2f}"

                items.append({"name": item.name, "type": item_type, "size": item_size if item_size > "00" else ''})
        except OSError:
            abort(500, description="Failed to read directory contents.")
        
        return sorted(items, key=lambda x: (x["type"] == "file", x["name"].lower()))
    
    def _get_readme_content(self, folder_path):
        """Gets rendered README.md content if it exists."""
        readme_path = folder_path / "README.md"
        if readme_path.is_file():
            try:
                with open(readme_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Basic markdown rendering - convert to HTML
                    return markdown.markdown(content)
            except (IOError, UnicodeDecodeError):
                return None
        return None
    
    def _get_safe_path(self, *path_parts):
        """Creates a safe path within BASE_DIR to prevent directory traversal."""
        # Join path parts and resolve to prevent directory traversal
        full_path = Path(BASE_DIR).joinpath(*path_parts).resolve()
        
        # Ensure the path is within BASE_DIR
        if not str(full_path).startswith(str(Path(BASE_DIR).resolve())):
            abort(400, description="Invalid path.")
        
        return full_path
    
    def _bytes_to_megabytes(self, bytes_value):
        """Converts a given value in bytes to megabytes."""
        if bytes_value < 0:
            raise ValueError("Bytes value cannot be negative.")
        return bytes_value / (1024 * 1024)