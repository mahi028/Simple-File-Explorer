import os
import platform
from dotenv import load_dotenv
load_dotenv()

# Get the OS type and absolute path of the root directory
os_type = platform.system()
root_directory = os.path.abspath(os.sep)
user_name = os.getenv('OS_USER_NAME')
user_directory = os.path.join(root_directory, 'users', user_name)

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), user_directory ))

from flask_restful import Api
from api.logic import *
api = Api()

# Route registration for Flask-RESTful
api.add_resource(FileResource, '/bucket/file/<path:path>')
api.add_resource(FolderResource, '/bucket/folder/', '/bucket/folder/<path:path>')


