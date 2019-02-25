import jwt
import json

from flask import Blueprint, request, jsonify
from app.service.user_authenticator import UserAuthenticator
from app.repository.user_repository import UserRepository
from app.models.user import User
from app.service.serialize import serialize
from app.token_required import token_required
from app.service.dotdict import dotdict

users_blueprint = Blueprint("users", __name__)


@users_blueprint.route("/users", methods=("GET",))
@token_required
def get_users(*args, **kwargs):
    users = UserRepository.query.all()
    return jsonify(serialize(users)), 200


@users_blueprint.route("/user/<int:user_id>", methods=("GET",))
@token_required
def get_user(user_id, *args, **kwargs):
    user = UserRepository.query.get(user_id)
    return jsonify(serialize(user)), 200


@users_blueprint.route("/user", methods=("POST",))
@token_required
def save_user(*args, **kwargs):
    data = dotdict(request.get_json())
    user = UserRepository.get(data.id)
    user.update(**data)
    UserRepository.save(user)
    return jsonify(serialize(user)), 201
