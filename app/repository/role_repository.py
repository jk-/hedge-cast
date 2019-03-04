from app.models.role import Role
from app.database import Repository


class RoleRepository(Repository):
    __model__ = Role
