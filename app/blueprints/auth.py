import jwt
from datetime import datetime, timedelta

from flask import Blueprint, request, current_app, jsonify
from app.service.user_authenticator import UserAuthenticator
from app.repository.user_repository import UserRepository
from app.models.user import User
from app.exception import InvalidAuthUser

auth_blueprint = Blueprint("auth", __name__)


@auth_blueprint.route("/register", methods=("POST",))
def register():
    data = request.get_json()
    user = User()
    user.set_username(data.username)
    user.set_password(data.pasword)
    user.set_email(data.email)
    user = UserRepository.save(user)
    return jsonify(user.to_dict()), 201


@auth_blueprint.route("/login", methods=("POST",))
def login():
    data = request.get_json()
    user = UserAuthenticator.authenticate(**data)

    if not user:
        raise InvalidAuthUser("Invalid Auth User")

    token = jwt.encode(
        {
            "sub": user.username,
            "iat": datetime.utcnow(),
            "exp": datetime.utcnow() + timedelta(minutes=10),
        },
        current_app.config["SECRET_KEY"],
        algorithm="HS256",
    )
    return jsonify({"token": token.decode("UTF-8")})
