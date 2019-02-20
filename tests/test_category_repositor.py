import pytest

from app.models.category import Category
from app.database import Repository
from app.repository.category_repository import CategoryRepository
from unittest.mock import patch


class TestCategoryRepository:
    @pytest.mark.smoke
    def test_init(self):
        assert issubclass(CategoryRepository, Category)
        assert issubclass(CategoryRepository, Repository)

    @pytest.mark.parametrize(
        "invalid_type, expected", [({}, None), ([], None), ((), None)]
    )
    @patch("flask_sqlalchemy._QueryProperty.__get__")
    def test_get_by_id(
        self, mocked_query_get, app_test, invalid_type, expected
    ):
        dummy = Category()
        dummy.name = "Category Name"
        mocked_query_get.return_value.get.return_value = dummy

        with app_test.app_context():
            first_category = CategoryRepository.get_by_id(1)
            assert isinstance(first_category, Category)
            assert first_category.name == "Category Name"
            assert not first_category.name == "Balls"

            invalid_category = CategoryRepository.get_by_id(invalid_type)
            assert invalid_category is expected
            assert not invalid_category
