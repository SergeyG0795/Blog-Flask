from wsgi import app
from blog.models.database import db


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print("done!")


@app.cli.command("create-users")
def create_users():
    from blog.models import User

    admin = User(username="admin", is_staff=True)
    james = User(username="James")

    db.session.add(admin)
    db.session.add(james)
    db.session.commit()

    print("done!")
