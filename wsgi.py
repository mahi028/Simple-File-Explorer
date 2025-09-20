from gunicorn.app.base import BaseApplication
from app import app

class StandaloneGunicorn(BaseApplication):
    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super().__init__()

    def load_config(self):
        for k, v in self.options.items():
            self.cfg.set(k.lower(), v)

    def load(self):
        return self.application

if __name__ == "__main__":
    options = {
        "bind": "0.0.0.0:9876",
        "workers": 2,
    }
    StandaloneGunicorn(app, options).run()