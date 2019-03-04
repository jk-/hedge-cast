from app.models.user_roles import UserRoles
from app.database import Repository


class UserRolesRepository(Repository):
    __model__ = UserRoles
