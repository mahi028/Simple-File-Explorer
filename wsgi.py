import signal
import sys
import time
from multiprocessing import Process
from waitress import serve
from webui import webui
from app import app
from flask import render_template
from assets.ascii_art import banner
from api import os_info, os_type, user_directory, CONFIG_FILE

LOACL_HOST = "127.0.0.1"
OPEN_HOST = "0.0.0.0"
BACKEND_PORT = 9876

web_window = webui.Window()
with app.app_context():
    webui_html = render_template("webUI.html")

def run_webui():
    web_window.show(webui_html)
    webui.wait()

def run_backend():
    serve(app, host=OPEN_HOST, port=BACKEND_PORT)

if __name__ == "__main__":
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
    print(f"Visit app on local address: http://{LOACL_HOST}:{BACKEND_PORT}/")
    print(f"Visit app on network: http://your-device-ip:{BACKEND_PORT}/")
    print("Note: Closing the UI window doesn't stop the application.")
    print("Note: Press \"CTRL + C\" to terminate the app.")

    # Start both processes
    p1 = Process(target=run_webui)
    p2 = Process(target=run_backend)

    p1.start()
    p2.start()

    def shutdown(sig, frame):
        print("\nShutting down gracefully...")
        p1.terminate()
        p2.terminate()
        p1.join()
        p2.join()
        sys.exit(0)

    # Register signals for CTRL+C and termination
    signal.signal(signal.SIGINT, shutdown)
    signal.signal(signal.SIGTERM, shutdown)

    # Windows-safe way to wait
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        shutdown(None, None)
