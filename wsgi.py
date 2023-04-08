from flask import render_template
from blog.models.database import db
from blog.app import create_app
import os

app = create_app()


cfg_name = os.environ.get("CONFIG_NAME") or "ProductionConfig"
app.config.from_object(f"blog.configs.{cfg_name}")


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        debug=True
    )


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
