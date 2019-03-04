from app.repository.user_repository import UserRepository


class UserAuthenticator:
    @staticmethod
    def authenticate(**kwargs):
        username = kwargs.get("username")
        password = kwargs.get("password")

        if not username or not password:
            return None

        user = UserRepository.first(username=username)
        if not user or not user.check_password(password):
            return None

        return user
