import os
import platform
from .config import config_vars

user_name = config_vars['OS_USER_NAME']
if not user_name:
    raise Exception("Please set you user name in config.py file. See config.example.py for refrence.")
print('USER Name: ', user_name)

os_type = platform.system()
print("OS Type: ", os_type)

os_info = platform.platform()
print("OS INFO: ", os_info)

match os_type:
    case 'Windows':
        root_directory = os.path.abspath(os.sep)
        print("Root Directory: ", root_directory)
        user_directory = os.path.join(root_directory, 'users', user_name)
    case 'Linux':
        user_directory = os.path.join('/home', user_name)
    case 'Darwin':
        user_directory = os.path.join('/Users', user_name)
    case '_':
        raise Exception("Your OS is not supported for this application Right now!")

print("User Directory: ", user_directory)

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), user_directory ))

from flask_restful import Api
from api.logic import *
api = Api()

# Route registration for Flask-RESTful
api.add_resource(FileResource, '/bucket/file/<path:path>')
api.add_resource(FolderResource, '/bucket/folder/', '/bucket/folder/<path:path>')


