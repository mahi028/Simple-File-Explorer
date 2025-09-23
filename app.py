"""This application is just a web base file explorer"""

from flask import Flask, render_template, send_from_directory
from api import api
from flask_cors import CORS

# Changing how jinja2 interprets delimiters
CUSTOM_JINJA_DELIMS = {
    'variable_start_string': '[[',
    'variable_end_string': ']]',
    'block_start_string': '{%',
    'block_end_string': '%}',
    'comment_start_string': '{#',
    'comment_end_string': '#}'
}
app = Flask(__name__, template_folder='templates')
for k, v in CUSTOM_JINJA_DELIMS.items():
    setattr(app.jinja_env, k, v)


CORS(app, allow_origins=["*"])
api.init_app(app)



# Serve the frontend
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/health")
def health():
    return {"msg":"Backend Running"}

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9876)
