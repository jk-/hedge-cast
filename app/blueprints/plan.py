import jwt
import json

from flask import Blueprint, request, jsonify
from app.repository.plan_repository import PlanRepository
from app.models.plan import Plan
from app.util.serialize import serialize
from app.util.token_required import token_required
from app.util.dotdict import dotdict
from app.validator.plan import PlanValidator


plan_blueprint = Blueprint("plans", __name__)


@plan_blueprint.route("/plans", methods=("GET",))
def get_plans(*args, **kwargs):
    plans = PlanRepository.query.all()
    return jsonify(serialize(plans)), 200


@plan_blueprint.route("/plan/<int:plan_id>", methods=("GET",))
def get_plan(plan_id, *args, **kwargs):
    plan = PlanRepository.query.get(plan_id)
    return jsonify(serialize(plan)), 200


admin_plan_blueprint = Blueprint("admin_plans", __name__)


@admin_plan_blueprint.before_request
@token_required(roles=["ROLE_ADMIN"])
def before_request(*args, **kwargs):
    """ Protect all of the admin endpoints. """
    pass


@admin_plan_blueprint.route("/plan", methods=("POST",))
def save_plan(*args, **kwargs):
    data = request.get_json()
    validator = PlanValidator(**data, csrf_enabled=False)

    if not validator.validate():
        raise Exception(validator.errors)

    data = dotdict(data)
    if not data.id:
        plan = Plan()
    else:
        plan = PlanRepository.get(data.id)
    plan.update(**data)
    PlanRepository.save(plan)
    return jsonify(serialize(plan)), 201


@admin_plan_blueprint.route("/plan/<int:plan_id>", methods=("DELETE",))
def delete_plan(plan_id, *args, **kwargs):
    plan = PlanRepository.query.get(plan_id)
    if plan:
        PlanRepository.delete(plan)
    return jsonify({"message": "Plan deleted.", "type": "success"}), 200
