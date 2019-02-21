from app.models.user_roles import UserRoles
from app.database import Repository


class UserRolesRepository(UserRoles, Repository):
    pass
