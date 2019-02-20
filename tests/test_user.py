import pytest

from app.models.user import User
from unittest.mock import patch


class TestUserModel:
    @pytest.mark.smoke
    def test_model_init(self):
        assert isinstance(User(), User)

    @patch("app.extensions.bcrypt.generate_password_hash")
    def test_set_passwrd(self, mocked_bcrypt):
        mocked_bcrypt.return_value.decode.return_value = "mocked password"
        user = User()
        user.set_password("password")
        assert user.password == "mocked password"

    def test_check_password(self):
        user = User()
        user.set_password("password")
        assert not user.check_password("")
        assert not user.check_password("password1")
        assert user.check_password("password")
