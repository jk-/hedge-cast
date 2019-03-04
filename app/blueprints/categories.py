from flask import Blueprint, request, jsonify
from app.repository.category_repository import CategoryRepository
from app.models.category import Category
from app.util.serialize import serialize
from app.util.dotdict import dotdict
from app.util.token_required import token_required
from app.validator.category import CategoryValidator

category_blueprint = Blueprint("category", __name__)


@category_blueprint.route("/categories", methods=("GET",))
def get_categories(*args, **kwargs):
    categories = CategoryRepository.all()
    return jsonify(serialize(categories)), 200


@category_blueprint.route("/category/<int:category_id>", methods=("GET",))
def get_category(category_id, *args, **kwargs):
    category_id = CategoryRepository.get(category_id)
    return jsonify(serialize(category_id)), 200


admin_category_blueprint = Blueprint("admin_category", __name__)


@admin_category_blueprint.before_request
@token_required(roles=["ROLE_ADMIN"])
def before_request(*args, **kwargs):
    """ Protect all of the admin endpoints. """
    pass


@admin_category_blueprint.route("/category", methods=("POST",))
def update_category(*args, **kwargs):
    data = request.get_json()
    validator = CategoryValidator(**data, csrf_enabled=False)

    if not validator.validate():
        raise Exception(validator.errors)

    data = dotdict(data)
    if not data.id:
        category = Category()
    else:
        category = CategoryRepository.get(data.id)
    category.update(**data)
    CategoryRepository.save(category)
    return jsonify(serialize(category)), 201


@admin_category_blueprint.route(
    "/category/<int:category_id>", methods=("DELETE",)
)
def delete_category(category_id, *args, **kwargs):
    category = CategoryRepository.get(category_id)
    if category:
        CategoryRepository.delete(category)
    return jsonify({"message": "Category deleted.", "type": "success"}), 200
