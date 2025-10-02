"""This application is just a web base file explorer"""

from flask import Flask, render_template
from api import api
from flask_cors import CORS
import socket

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

HOST = get_local_ip()
OPEN_HOST = "0.0.0.0"
PORT = 9876

# Changing how jinja2 interprets delimiters
CUSTOM_JINJA_DELIMS = {
    'variable_start_string': '[[',
    'variable_end_string': ']]',
    'block_start_string': '{%',
    'block_end_string': '%}',
    'comment_start_string': '{#',
    'comment_end_string': '#}'
}
app = Flask(__name__, template_folder='templates', static_folder='static')
for k, v in CUSTOM_JINJA_DELIMS.items():
    setattr(app.jinja_env, k, v)


CORS(app, allow_origins=["*"])
api.init_app(app)

@app.route("/")
def index():
    return render_template("index.html", host = HOST, port = PORT, webUI = False)

@app.route("/player")
def media_player():
    return render_template("mediaPlayer.html", host = HOST, port = PORT, webUI = False)

@app.route("/health")
def health():
    return {"msg":"Backend Running"}

if __name__ == "__main__":
    app.run(debug=True, host=OPEN_HOST, port=PORT)
