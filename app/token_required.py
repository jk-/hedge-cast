import jwt

from functools import wraps
from flask import request, current_app, jsonify
from app.repository.user_repository import UserRepository


def token_required(f):
    @wraps(f)
    def _verify(*args, **kwargs):
        auth_headers = request.headers.get("Authorization", "").split()

        invalid_msg = {
            "message": "Authentication required",
            "authenticated": False,
        }

        if len(auth_headers) != 2:
            return jsonify(invalid_msg), 401

        try:
            token = auth_headers[1]
            data = jwt.decode(token, current_app.config["SECRET_KEY"])
            user = UserRepository.query.filter_by(username=data["sub"]).first()
            if not user:
                raise RuntimeError("User not found")
            return f(requesting_user=user, *args, **kwargs)
        except jwt.ExpiredSignatureError:
            return (jsonify(invalid_msg), 401)
        except (jwt.InvalidTokenError, Exception) as e:
            print(e)
            return jsonify(invalid_msg), 401

    return _verify
