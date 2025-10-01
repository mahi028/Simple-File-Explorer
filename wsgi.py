import signal
import sys
import time
from multiprocessing import Process, freeze_support
from waitress import serve
from webui import webui
from app import app, HOST, PORT
from flask import render_template
from assets.ascii_art import banner
from api import os_info, os_type, user_directory, CONFIG_FILE

def run_webui(webui_html):
    web_window = webui.Window()
    web_window.show(webui_html)
    webui.wait()

def run_backend():
    serve(app, host=HOST, port=PORT)

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
    print("Note: Closing the UI window doesn't stop the application.")
    print("Note: Press \"CTRL + C\" to terminate the app.")

if __name__ == "__main__":
    if sys.argv[-1] == "nogui":
        print_info()
        run_backend()

    else:
        freeze_support()
        print_info()

        with app.app_context():
            webui_html = render_template("index.html", host=HOST, port=PORT, webUI=True)

        p1 = Process(target=run_webui, args=(webui_html,))
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

        signal.signal(signal.SIGINT, shutdown)
        signal.signal(signal.SIGTERM, shutdown)

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            shutdown(None, None)
        