from waitress import serve
from app import app

if __name__ == "__main__":
    print("Application running on all networks")
    print("Visit app on local address: http://127.0.0.1:9876/")
    print("Visit app on network: http://your-device-ip:9876/")
    serve(app, host="0.0.0.0", port=9876)
