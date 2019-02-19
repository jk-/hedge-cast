import pytest

from app.models.user import User


class TestUserModel(object):

    def test_model_init(self):
        user = User('password')
        assert False
        assert user.password == 'a'
