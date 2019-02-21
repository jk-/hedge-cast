import pytest

from app.models.user_roles import UserRoles
from app.database import Repository
from app.repository.user_roles_repository import UserRolesRepository
from unittest.mock import patch


class TestUserRolesRepository:
    @pytest.mark.smoke
    def test_init(self):
        assert issubclass(UserRolesRepository, UserRoles)
        assert issubclass(UserRolesRepository, Repository)

    @pytest.mark.parametrize(
        "invalid_type, expected", [({}, None), ([], None), ((), None)]
    )
    @patch("flask_sqlalchemy._QueryProperty.__get__")
    def test_get_by_id(
        self, mocked_query_get, app_test, invalid_type, expected
    ):
        dummy = UserRoles()
        dummy.role_id = 1
        dummy.user_id = 2
        mocked_query_get.return_value.get.return_value = dummy

        with app_test.app_context():
            first_user_roles = UserRolesRepository.get_by_id(1)
            assert isinstance(first_user_roles, UserRoles)
            assert first_user_roles.role_id == 1
            assert first_user_roles.user_id == 2

            invalid_user_roles = UserRolesRepository.get_by_id(invalid_type)
            assert invalid_user_roles is expected
            assert not invalid_user_roles
