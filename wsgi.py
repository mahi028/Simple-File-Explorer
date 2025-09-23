from assets.ascii_art import banner
print(banner)

from waitress import serve
from webui import webui
from app import app
import threading
from webuiTemplate import template

LOACL_HOST = "127.0.0.1"
OPEN_HOST = "0.0.0.0"
BACKEND_PORT = 9876
WEBUI_PORT = 9877

web_window = webui.Window()

if __name__ == "__main__":
    # Print some info
    print("Application running on all networks")
    print(f"Visit app on local address: http://{LOACL_HOST}:{BACKEND_PORT}/")
    print(f"Visit app on network: http://your-device-ip:{BACKEND_PORT}/")
    print("Note: Closing the UI window doesn't stop the application.")
    print("Note: Press \"CTRL + C\" to terminate the app.")
    
    # Open the web window
    web_window.show(template)
    threading.Timer(0.5, lambda: webui.wait()).start()
    
    # Serve the app
    serve(app, host=OPEN_HOST, port=BACKEND_PORT)
