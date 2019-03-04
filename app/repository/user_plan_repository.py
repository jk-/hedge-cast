from app.models.user_plan import UserPlan
from app.database import Repository


class UserPlanRepository(Repository):
    __model__ = UserPlan
