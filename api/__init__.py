import os
import platform
import json
from .config import config_vars
from pathlib import Path

os_type = platform.system()
print("OS Type: ", os_type)

os_info = platform.platform()
print("OS INFO: ", os_info)

user_directory = Path.home()
print("User Directory: ", user_directory)

match os_type:
    case 'Windows':
        appdata = os.path.join(user_directory, 'AppData/Roaming')
    case 'Linux':
        appdata = os.path.join(user_directory, '.config')
    case 'Darwin':
        appdata = os.path.join(user_directory, 'AppData/Roaming')
    case '_':
        raise Exception("Your OS is not supported by this application Right now!")
    

# Store the config in appdata
config_dir = os.path.join(appdata, "SFX")
os.makedirs(config_dir, exist_ok=True)

CONFIG_FILE = os.path.join(config_dir, "config.json")

print('Config File at: ', CONFIG_FILE)
# if not os.path.exists(CONFIG_FILE):
#     with open(CONFIG_FILE, "w") as f:
#         json.dump(config_vars, f)
# else:
#     with open(CONFIG_FILE) as f:
#         config = json.load(f)



BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), user_directory ))

from flask_restful import Api
from api.logic import *
api = Api()

# Route registration for Flask-RESTful
api.add_resource(FileResource, '/bucket/file/<path:path>')
api.add_resource(FolderResource, '/bucket/folder/', '/bucket/folder/<path:path>')


