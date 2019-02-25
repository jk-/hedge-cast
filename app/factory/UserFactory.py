from app.models.user import User


class UserFactory:
    @staticmethod
    def create_from_json(json):
        user = User(**json)
        return user
