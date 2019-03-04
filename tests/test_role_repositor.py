import pytest

from app.models.role import Role
from app.database import Repository
from app.repository.role_repository import RoleRepository
from unittest.mock import patch


class TestRoleRepository:
    @pytest.mark.smoke
    def test_init(self):
        assert RoleRepository._isinstance(Role(), raise_error=False)

    @patch("flask_sqlalchemy._QueryProperty.__get__")
    def test_get(self, mocked_query_get, app_test):
        dummy = Role()
        mocked_query_get.return_value.get.return_value = dummy

        with app_test.app_context():
            first_role = RoleRepository.get(1)
            assert isinstance(first_role, Role)
