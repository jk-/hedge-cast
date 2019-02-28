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
def populate_users(num_users):
    """Populates the database with seed data."""
    fake = Faker()
    users = []
    admin_role = Role(name="ROLE_ADMIN")
    for _ in range(num_users):
        user = User()
        user.username = fake.word()
        user.password = fake.word()
        user.email = fake.email()
        users.append(user)
    jonUser = User()
    jonUser.username = "jon"
    jonUser.password = "pass"
    jonUser.email = "jon@stonetorch.com"
    jonUser.roles = [admin_role]
    users.append(jonUser)
    for user in users:
        print("saving user {}".format(user))
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
        print("saving category {}".format(cat))
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
        print("saving plan {}".format(plan))
        db.session.add(plan)
    db.session.commit()


def populate_playlist():
    """Populates the database with seed data."""
    fake = Faker()
    playlists = []
    for _ in range(5):
        _playlist = Playlist()
        _playlist.name = fake.word()
        _playlist.enabled = fake.boolean()
        playlists.append(_playlist)
    for playlist in playlists:
        print("saving playlist {}".format(playlist))
        db.session.add(playlist)
    db.session.commit()


def populate_videos():
    """Populates the database with seed data."""
    fake = Faker()
    videos = []
    for _ in range(5):
        _video = Video()
        _video.title = fake.word()
        _video.access_type = fake.word()
        _video.enabled = fake.boolean()
        _video.url = fake.url()
        _video.source = fake.word()
        _video.thumbnail = fake.word()
        videos.append(_video)
    for video in videos:
        print("saving video {}".format(video))
        db.session.add(video)
    db.session.commit()


def drop_db():
    """Drops the database."""
    if click.confirm("Are you sure?", abort=True):
        db.drop_all()
