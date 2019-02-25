import jwt
import json

from flask import Blueprint, request, jsonify
from app.repository.plan_repository import PlanRepository
from app.models.plan import Plan
from app.service.serialize import serialize
from app.token_required import token_required
from app.service.dotdict import dotdict


plan_blueprint = Blueprint("plans", __name__)


@plan_blueprint.route("/plans", methods=("GET",))
@token_required
def get_plans(*args, **kwargs):
    plans = PlanRepository.query.all()
    return jsonify(serialize(plans)), 200


@plan_blueprint.route("/plan/<int:plan_id>", methods=("GET",))
@token_required
def get_plan(plan_id, *args, **kwargs):
    plan = PlanRepository.query.get(plan_id)
    return jsonify(serialize(plan)), 200


@plan_blueprint.route("/plan", methods=("POST",))
@token_required
def save_plan(*args, **kwargs):
    data = dotdict(request.get_json())
    plan = PlanRepository.get(data.id)
    plan.update(**data)
    PlanRepository.save(plan)
    return jsonify(serialize(plan)), 201
