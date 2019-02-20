import pytest

from app.models.user_plan import UserPlan
from app.database import Repository
from app.repository.user_plan_repository import UserPlanRepository
from unittest.mock import patch


class TestUserPlanRepository:
    @pytest.mark.smoke
    def test_init(self):
        assert issubclass(UserPlanRepository, UserPlan)
        assert issubclass(UserPlanRepository, Repository)

    @pytest.mark.parametrize(
        "invalid_type, expected", [({}, None), ([], None), ((), None)]
    )
    @patch("flask_sqlalchemy._QueryProperty.__get__")
    def test_get_by_id(
        self, mocked_query_get, app_test, invalid_type, expected
    ):
        dummy = UserPlan()
        dummy.user_id = 1
        dummy.plan_id = 2
        mocked_query_get.return_value.get.return_value = dummy

        with app_test.app_context():
            first_user_plan = UserPlanRepository.get_by_id(1)
            assert isinstance(first_user_plan, UserPlan)
            assert first_user_plan.user_id == 1
            assert first_user_plan.plan_id == 2

            invalid_user_plan = UserPlanRepository.get_by_id(invalid_type)
            assert invalid_user_plan is expected
            assert not invalid_user_plan
