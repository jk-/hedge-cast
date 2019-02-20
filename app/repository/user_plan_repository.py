from app.models.user_plan import UserPlan
from app.database import Repository


class UserPlanRepository(UserPlan, Repository):
    pass
