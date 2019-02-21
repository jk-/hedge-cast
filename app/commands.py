from faker import Faker
import click

from app.database import db
from app.models.user import User
from app.models.role import Role
from app.models.user_roles import UserRoles
from app.models.plan import Plan
from app.models.category import Category
from app.models.playlist import Playlist
from app.models.video import Video
from app.models.playlist_category import PlaylistCategory
from app.models.user_plan import UserPlan
from app.models.video_playlist import VideoPlaylist


def create_db():
    """Creates the tables."""
    db.create_all()


@click.option("--num_users", default=5, help="Number of users.")
def populate_db(num_users):
    """Populates the database with seed data."""
    fake = Faker()
    users = []
    admin_role = Role(name="ROLE_ADMIN")
    for _ in range(num_users):
        _user = User()
        _user.set_password(fake.word() + fake.word())
        _user.set_email(fake.email())
        _user.set_username(fake.user_name())
        users.append(_user)
    jonUser = User()
    jonUser.set_password("pass")
    jonUser.set_email("jon@stonetorch.com")
    jonUser.set_username("jon")
    jonUser.roles = [admin_role]
    users.append(jonUser)
    for user in users:
        print("saving user %s".format(user))
        db.session.add(user)
    db.session.commit()


def drop_db():
    """Drops the database."""
    if click.confirm("Are you sure?", abort=True):
        db.drop_all()
