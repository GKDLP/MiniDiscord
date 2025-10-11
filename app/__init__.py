# app/__init__.py
from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO()

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "dev-secret-key"

    @app.route('/')
    def home():
        return "Hello Mini Discord 👋"

    socketio.init_app(app)
    return app
