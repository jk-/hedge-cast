import pytest

from app.models.user import User


class UserModel(object):

    def test_model_init(self):
        user = User('password')
        assert user.password == 'a'
