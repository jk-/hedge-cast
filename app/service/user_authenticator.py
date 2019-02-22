from app.repository.user_repository import UserRepository


class UserAuthenticator(UserRepository):
    @staticmethod
    def authenticate(**kwargs):
        username = kwargs.get("username")
        password = kwargs.get("password")

        if not username or not password:
            return None

        user = UserRepository.query.filter_by(username=username).first()
        if not user or not user.check_password(password):
            return None

        return user
