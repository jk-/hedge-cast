import jwt
import json

from flask import Blueprint, request, jsonify
from app.repository.plan_repository import PlanRepository
from app.models.plan import Plan
from app.service.serialize import serialize
from app.token_required import token_required

plan_blueprint = Blueprint("plans", __name__)


@plan_blueprint.route("/plans", methods=("GET",))
@token_required
def get_plans(*args, **kwargs):
    plans = PlanRepository.query.all()
    return jsonify(serialize(plans)), 201


@plan_blueprint.route("/plan/<int:plan_id>", methods=("GET",))
@token_required
def get_plan(plan_id, *args, **kwargs):
    plan = PlanRepository.query.get(plan_id)
    return jsonify(serialize(plan)), 201
