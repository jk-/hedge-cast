from app.models.user import User
from app.database import Repository


class UserRepository(User, Repository):
    pass
