from flask import Flask
from backend.routes.health import health_bp
from backend.routes.users import users_bp
from backend.routes.error import error_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(health_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(error_bp)
    return app