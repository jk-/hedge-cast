from app.database import db
from app.models.user import User

def create_db():
    """Creates the tables."""
    db.create_all()
