import pytest

from app.models.plan import Plan
from app.database import Repository
from app.repository.plan_repository import PlanRepository
from unittest.mock import patch


class TestPlanRepository:
    @pytest.mark.smoke
    def test_init(self):
        assert issubclass(PlanRepository, Plan)
        assert issubclass(PlanRepository, Repository)

    @pytest.mark.parametrize(
        "invalid_type, expected", [({}, None), ([], None), ((), None)]
    )
    @patch("flask_sqlalchemy._QueryProperty.__get__")
    def test_get_by_id(
        self, mocked_query_get, app_test, invalid_type, expected
    ):
        dummy = Plan()
        dummy.name = "Plan Name"
        mocked_query_get.return_value.get.return_value = dummy

        with app_test.app_context():
            first_plan = PlanRepository.get_by_id(1)
            assert isinstance(first_plan, Plan)
            assert first_plan.name == "Plan Name"
            assert not first_plan.name == "Balls"

            invalid_plan = PlanRepository.get_by_id(invalid_type)
            assert invalid_plan is expected
            assert not invalid_plan
