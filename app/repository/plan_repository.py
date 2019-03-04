from app.database import Repository
from app.models.plan import Plan


class PlanRepository(Repository):
    __model__ = Plan
