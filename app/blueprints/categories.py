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
def get_categories(*args, **kwargs):
    categories = CategoryRepository.query.all()
    return jsonify(serialize(categories)), 201


@category_blueprint.route("/category/<int:category_id>", methods=("GET",))
@token_required
def get_category(category_id, *args, **kwargs):
    category_id = CategoryRepository.query.get(category_id)
    return jsonify(serialize(category_id)), 201
