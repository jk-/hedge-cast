from app.models.role import Role
from app.database import Repository


class RoleRepository(Role, Repository):
    @staticmethod
    def get_by_name(name):
        if isinstance(name, str):
            return Role.query.filter_by(name=name).first()
        return None
