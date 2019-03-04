import pytest

from app.models.user_plan import UserPlan
from app.database import Repository
from app.repository.user_plan_repository import UserPlanRepository
from unittest.mock import patch


class TestUserPlanRepository:
    @pytest.mark.smoke
    def test_init(self):
        assert UserPlanRepository._isinstance(UserPlan(), raise_error=False)

    @patch("flask_sqlalchemy._QueryProperty.__get__")
    def test_get(self, mocked_query_get, app_test):
        dummy = UserPlan()
        mocked_query_get.return_value.get.return_value = dummy

        with app_test.app_context():
            first_user_plan = UserPlanRepository.get(1)
            assert isinstance(first_user_plan, UserPlan)
