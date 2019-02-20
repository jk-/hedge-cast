from app.models.user import User
from app.database import Repository
from app.repository.user_repository import UserRepository
from app import create_app, config


class TestUserRepository(object):
    def test_init(self):
        assert issubclass(UserRepository, User)
        assert issubclass(UserRepository, Repository)

    def test_get_by_id(self):
        app = create_app(config.base_config)

        with app.app_context():
            user = UserRepository.get_by_id(1)
            assert user.username == "nealalan"
