from app.models.role import Role
from app.database import Repository


class RoleRepository(Role, Repository):
    pass
