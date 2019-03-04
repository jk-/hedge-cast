import pytest

from app.models.user_roles import UserRoles
from app.database import Repository
from app.repository.user_roles_repository import UserRolesRepository
from unittest.mock import patch


class TestUserRolesRepository:
    @pytest.mark.smoke
    def test_init(self):
        assert UserRolesRepository._isinstance(UserRoles(), raise_error=False)

    @patch("flask_sqlalchemy._QueryProperty.__get__")
    def test_get(self, mocked_query_get, app_test):
        dummy = UserRoles()
        mocked_query_get.return_value.get.return_value = dummy

        with app_test.app_context():
            first_user_roles = UserRolesRepository.get(1)
            assert isinstance(first_user_roles, UserRoles)
