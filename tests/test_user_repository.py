import pytest

from app.models.user import User
from app.database import Repository
from app.repository.user_repository import UserRepository
from unittest.mock import patch


class TestUserRepository:
    @pytest.mark.smoke
    def test_init(self):
        assert UserRepository._isinstance(User(), raise_error=False)

    @patch("flask_sqlalchemy._QueryProperty.__get__")
    def test_get(self, mocked_query_get, app_test):
        dummy = User()
        mocked_query_get.return_value.get.return_value = dummy

        with app_test.app_context():
            first_user = UserRepository.get(1)
            assert isinstance(first_user, User)
