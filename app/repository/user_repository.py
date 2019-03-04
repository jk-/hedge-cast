from app.models.user import User
from app.database import Repository


class UserRepository(Repository):
    __model__ = User
