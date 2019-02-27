import jwt

from functools import wraps
from flask import request, current_app, jsonify
from app.repository.user_repository import UserRepository
from app.models.exception import InvalidToken
from app.models.exception import AuthRequired
from app.models.exception import InvalidAuthUser


def token_required(f):
    @wraps(f)
    def _verify(*args, **kwargs):
        auth_headers = request.headers.get("Authorization", "").split()

        if len(auth_headers) != 2:
            raise AuthRequired("Authentication required")

        try:
            token = auth_headers[1]
            data = jwt.decode(token, current_app.config["SECRET_KEY"])
            user = UserRepository.query.filter_by(username=data["sub"]).first()
            if not user:
                raise InvalidAuthUser("Unathorized User")
            return f(requesting_user=user, *args, **kwargs)
        except jwt.ExpiredSignatureError:
            raise InvalidToken("Expired Signature")
        except (jwt.InvalidTokenError, Exception) as e:
            raise Exception(e)

    return _verify
