import jwt
import json

from flask import Blueprint, request, jsonify
from app.repository.role_repository import RoleRepository
from app.models.role import Role
from app.service.serialize import serialize
from app.token_required import token_required

roles_blueprint = Blueprint("roles", __name__)


@roles_blueprint.route("/roles", methods=("GET",))
@token_required
def get_roles(*args, **kwargs):
    roles = RoleRepository.query.all()
    return jsonify(serialize(roles)), 200


@roles_blueprint.route("/role/<int:role_id>", methods=("GET",))
@token_required
def get_role(role_id, *args, **kwargs):
    role = RoleRepository.query.get(role_id)
    return jsonify(serialize(role)), 200
