from flask import Blueprint, request, jsonify
from app.repository.user_repository import UserRepository
from app.repository.role_repository import RoleRepository
from app.models.user import User
from app.util.serialize import serialize
from app.util.token_required import token_required
from app.util.dotdict import dotdict
from app.util.user_authenticator import UserAuthenticator
from app.validator.user import UserValidator

users_blueprint = Blueprint("users", __name__)


@users_blueprint.route("/users", methods=("GET",))
def get_users(*args, **kwargs):
    users = UserRepository.all()
    return jsonify(serialize(users)), 200


@users_blueprint.route("/user/<int:user_id>", methods=("GET",))
def get_user(user_id, *args, **kwargs):
    user = UserRepository.get(user_id)
    return jsonify(serialize(user)), 200


admin_users_blueprint = Blueprint("admin_users", __name__)


@admin_users_blueprint.before_request
@token_required(roles=["ROLE_ADMIN"])
def before_request(*args, **kwargs):
    """ Protect all of the admin endpoints. """
    pass


@admin_users_blueprint.route("/user", methods=("POST",))
def save_user(*args, **kwargs):
    data = request.get_json()
    user_validator = UserValidator(**data, csrf_enabled=False)

    if not user_validator.validate():
        raise Exception(user_validator.errors)

    data = dotdict(data)
    if not data.id:
        user = User()
    else:
        user = UserRepository.get(data.id)
    user.update(**data)

    user.roles = []

    for role in data.roles:
        _role = RoleRepository.first(name=role)
        user.roles.append(_role)

    UserRepository.save(user)

    return jsonify(serialize(user)), 201


@admin_users_blueprint.route("/user/<int:user_id>", methods=("DELETE",))
def delete_user(user_id, *args, **kwargs):
    user = UserRepository.get(user_id)
    if user:
        UserRepository.delete(user)
    return jsonify({"message": "User deleted.", "type": "success"}), 200
