from faker import Faker
import click

from app.database import db
from app.models.user import User
from app.models.role import Role
from app.models.user_roles import UserRoles
from app.models.plan import Plan
from app.models.category import Category
from app.models.plan import Plan
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
        _cat = User()
        _cat.set_password(fake.word() + fake.word())
        _cat.set_email(fake.email())
        _cat.set_catname(fake.user_name())
        users.append(_cat)
    jonUser = User()
    jonUser.set_password("pass")
    jonUser.set_email("jon@stonetorch.com")
    jonUser.set_catname("jon")
    jonUser.roles = [admin_role]
    users.append(jonUser)
    for user in users:
        print("saving user %s".format(user))
        db.session.add(user)
    db.session.commit()


def populate_category():
    """Populates the database with seed data."""
    fake = Faker()
    categories = []
    for _ in range(5):
        _cat = Category()
        _cat.name = fake.word()
        categories.append(_cat)
    for cat in categories:
        print("saving category %s".format(cat))
        db.session.add(cat)
    db.session.commit()


def populate_plans():
    """Populates the database with seed data."""
    fake = Faker()
    plans = []
    for _ in range(5):
        _plan = Plan()
        _plan.name = fake.word()
        _plan.enabled = fake.boolean()
        _plan.code = fake.word()
        _plan.interval_term = 1
        _plan.interval_count = 1
        _plan.price = 12.00
        _plan.trial_days = 0
        _plan.statement_desc = fake.word()
        _plan.plan_group = fake.word()
        plans.append(_plan)
    for plan in plans:
        print("saving plan %s".format(plan))
        db.session.add(plan)
    db.session.commit()


def drop_db():
    """Drops the database."""
    if click.confirm("Are you sure?", abort=True):
        db.drop_all()
