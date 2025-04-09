from flask import Flask
from backend.routes.health import health_bp
from backend.routes.users import users_bp
from backend.routes.error import error_bp
from backend.routes.auth import auth_bp
from backend.extensions import db

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = \
        "postgresql://longwei:my-password@localhost:5432/backenddb"

    db.app = app
    db.init_app(app)
    db.create_all()

    app.register_blueprint(auth_bp)
    app.register_blueprint(health_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(error_bp)
    return app