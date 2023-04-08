from flask import Flask
from flask_migrate import Migrate

from blog.models.database import db
from blog.security import flask_bcrypt
from blog.views.articles import articles_app
from blog.views.auth import auth_app, login_manager
from blog.views.users import users_app


def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = "abcdefg123456"

    db.init_app(app)

    register_blueprints(app)

    login_manager.init_app(app)

    migrate = Migrate(app, db, compare_type=True)

    flask_bcrypt.init_app(app)

    return app


def register_blueprints(app: Flask):
    app.register_blueprint(users_app, url_prefix="/users")
    app.register_blueprint(articles_app, url_prefix="/articles")
    app.register_blueprint(auth_app, url_prefix="/auth")


