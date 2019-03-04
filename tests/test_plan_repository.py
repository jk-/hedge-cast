import pytest

from app.models.plan import Plan
from app.database import Repository
from app.repository.plan_repository import PlanRepository
from unittest.mock import patch


class TestPlanRepository:
    @pytest.mark.smoke
    def test_init(self):
        assert True is PlanRepository._isinstance(Plan(), raise_error=False)

    @patch("flask_sqlalchemy._QueryProperty.__get__")
    def test_get(self, mocked_query_get, app_test):
        dummy = Plan()
        mocked_query_get.return_value.get.return_value = dummy

        with app_test.app_context():
            first_plan = PlanRepository.get(1)
            assert isinstance(first_plan, Plan)
