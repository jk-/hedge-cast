import jwt

from flask import Blueprint, request, jsonify
from app.service.user_authenticator import UserAuthenticator
from app.repository.user_repository import UserRepository
from app.models.user import User
from app.service.serialize import serialize
from app.token_required import token_required

users_blueprint = Blueprint("users", __name__)


@users_blueprint.route("/users", methods=("GET",))
@token_required
def get_users():
    users = UserRepository.query.all()
    return jsonify(serialize(users)), 201
