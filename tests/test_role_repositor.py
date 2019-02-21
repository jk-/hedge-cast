import pytest

from app.models.role import Role
from app.database import Repository
from app.repository.role_repository import RoleRepository
from unittest.mock import patch


class TestRoleRepository:
    @pytest.mark.smoke
    def test_init(self):
        assert issubclass(RoleRepository, Role)
        assert issubclass(RoleRepository, Repository)

    @pytest.mark.parametrize(
        "invalid_type, expected", [({}, None), ([], None), ((), None)]
    )
    @patch("flask_sqlalchemy._QueryProperty.__get__")
    def test_get_by_id(
        self, mocked_query_get, app_test, invalid_type, expected
    ):
        dummy = Role()
        dummy.name = "Role Name"
        mocked_query_get.return_value.get.return_value = dummy

        with app_test.app_context():
            first_role = RoleRepository.get_by_id(1)
            assert isinstance(first_role, Role)
            assert first_role.name == "Role Name"
            assert not first_role.name == "Balls"

            invalid_role = RoleRepository.get_by_id(invalid_type)
            assert invalid_role is expected
            assert not invalid_role
