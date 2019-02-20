import pytest

from app.models.user import User
from app.database import Repository
from app.repository.user_repository import UserRepository
from unittest.mock import patch


class TestUserRepository:
    @pytest.mark.smoke
    def test_init(self):
        assert issubclass(UserRepository, User)
        assert issubclass(UserRepository, Repository)

    @pytest.mark.parametrize(
        "invalid_type, expected", [({}, None), ([], None), ((), None)]
    )
    @patch("flask_sqlalchemy._QueryProperty.__get__")
    def test_get_by_id(
        self, mocked_query_get, app_test, invalid_type, expected
    ):
        dummy = User()
        dummy.id = 1
        dummy.username = "jon"
        mocked_query_get.return_value.get.return_value = dummy

        with app_test.app_context():
            first_user = UserRepository.get_by_id(1)
            assert isinstance(first_user, User)
            assert first_user.id == 1
            assert first_user.username == "jon"
            assert not first_user.username == "josh"

            invalid_user = UserRepository.get_by_id(invalid_type)
            assert invalid_user is expected
            assert not invalid_user
