from app.models.plan import Plan
from app.database import Repository


class PlanRepository(Plan, Repository):
    pass
