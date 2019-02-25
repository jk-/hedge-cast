import jwt
import json

from flask import Blueprint, request, jsonify
from app.repository.category_repository import CategoryRepository
from app.models.category import Category
from app.service.serialize import serialize
from app.token_required import token_required

category_blueprint = Blueprint("category", __name__)


@category_blueprint.route("/categories", methods=("GET",))
@token_required
def get_users(*args, **kwargs):
    categories = CategoryRepository.query.all()
    return jsonify(serialize(categories)), 201
