from waitress import serve
from app import app, HOST, PORT
from assets.ascii_art import banner
from api import os_info, os_type, user_directory, CONFIG_FILE

def run_backend():
    serve(app, host=HOST, port=PORT, threads=8, max_request_body_size=2**60 - 1)

def print_info():
    print(banner)
    print()
    print("-"*10+"OS INFORMATION"+"-"*10)
    print("OS Type: ", os_type)
    print("OS INFO: ", os_info)
    print("User Directory: ", user_directory)
    print('Config File at: ', CONFIG_FILE)
    print()
    print("-"*7+"NETWORK INFORMATION"+"-"*7)
    print("Application running on all networks")
    print(f"Visit app on local address: http://127.0.0.1:{PORT}/")
    print(f"Visit app on network: http://{HOST}:{PORT}/")
    print("Note: Press \"CTRL + C\" to terminate the app.")

if __name__ == "__main__":
    print_info()
    run_backend()