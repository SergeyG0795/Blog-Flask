import os.path

from flask import Flask, render_template
from flask_migrate import Migrate

from blog.admin import admin
from blog.api import init_api
from blog.configs import DevConfig
from blog.models.database import db
from blog.security import flask_bcrypt
from blog.views.articles import articles_app
from blog.views.auth import auth_app, login_manager
from blog.views.authors import authors_app
from blog.views.users import users_app


def create_app() -> Flask:
    app = Flask(__name__)


    cfg_name = os.environ.get("CONFIG_NAME") or "ProductionConfig"
    app.config.from_object(f"blog.configs.{cfg_name}")
    # db_path = os.path.abspath(os.getcwd()) + "blog.db"
    # app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db" + db_path
    # app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    # app.config["SECRET_KEY"] = "abcdefg123456"

    db.init_app(app)
    register_blueprints(app)
    login_manager.init_app(app)
    migrate = Migrate(app, db, compare_type=True)
    flask_bcrypt.init_app(app)
    admin.init_app(app)
    api = init_api(app)
    return app


def register_blueprints(app: Flask):
    app.register_blueprint(users_app, url_prefix="/users")
    app.register_blueprint(articles_app, url_prefix="/articles")
    app.register_blueprint(auth_app, url_prefix="/auth")
    app.register_blueprint(authors_app, url_prefix="/authors")


app = create_app()
# cfg_name = os.environ.get("CONFIG_NAME") or "ProductionConfig"
# app.config.from_object(f"blog.configs.{cfg_name}")


@app.route("/")
def index():
    return render_template("index.html")


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print("done!")


@app.cli.command("create-admin")
def create_admin():
    from blog.models import User

    admin = User(username="admin", is_staff=True)
    admin.password = os.environ.get("ADMIN_PASSWORD") or "adminpass"

    db.session.add(admin)
    db.session.commit()

    print("done!")


@app.cli.command("create-tags")
def create_tags():
    from blog.models import Tag
    for name in [
        "flask",
        "django",
        "python",
        "sqlalchemy",
        "news",
    ]:
        tag = Tag(name=name)
        db.session.add(tag)
    db.session.commit()
    print("done!")
