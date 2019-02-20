from faker import Faker
import click

from app.database import db
from app.models.user import User
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


@click.option('--num_users', default=5, help='Number of users.')
def populate_db(num_users):
    """Populates the database with seed data."""
    fake = Faker()
    users = []
    for _ in range(num_users):
        username = fake.user_name()
        email = fake.email()
        users.append(
            User(
                username=username,
                username_canonical=username,
                email=email,
                salt=fake.word(),
                email_canonical=email,
                email_reverse=email[:-1],
                password=fake.word() + fake.word()
            )
        )
    username = 'jon'
    email = 'jon@stonetorch.com'
    users.append(
        User(
            username=username,
            username_canonical=username,
            email=email,
            email_canonical=email,
            email_reverse=email[:-1],
            salt=fake.word(),
            password='pass',
            enabled=True,
            roles="ROLE_ADMIN"
        )
    )
    for user in users:
        print('saving user'.format(user))
        db.session.add(user)
    db.session.commit()
