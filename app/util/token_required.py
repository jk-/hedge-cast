import jwt

from functools import wraps
from flask import request, current_app, jsonify
from app.repository.user_repository import UserRepository
from app.exception import InvalidToken
from app.exception import AuthRequired
from app.exception import InvalidAuthUser


def token_required(roles=None):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            auth_headers = request.headers.get("Authorization", "").split()

            if len(auth_headers) != 2:
                raise AuthRequired(
                    "Session Expired. Please login to continue."
                )

            try:
                token = auth_headers[1]
                data = jwt.decode(token, current_app.config["SECRET_KEY"])
                user = UserRepository.find(username=data["sub"]).first()
                if not user:
                    raise InvalidAuthUser(
                        "You are unathorized to access this resource."
                    )
                user_roles = [x.name for x in user.roles]
                role_check = [role for role in roles if role not in user_roles]
                if len(role_check):
                    raise InvalidAuthUser(
                        "You are unathorized to access this resource."
                    )
                return f(requesting_user=user, *args, **kwargs)
            except jwt.ExpiredSignatureError:
                raise AuthRequired(
                    "Session Expired. Please login to continue."
                )
            except (jwt.InvalidTokenError, Exception) as e:
                raise Exception(e)

        return decorated_function

    return decorator
