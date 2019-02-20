import pytest

from app.models.playlist_category import PlaylistCategory
from app.database import Repository
from app.repository.playlist_category_repository import (
    PlaylistCategoryRepository,
)
from unittest.mock import patch


class TestPlaylistCategoryRepository:
    @pytest.mark.smoke
    def test_init(self):
        assert issubclass(PlaylistCategoryRepository, PlaylistCategory)
        assert issubclass(PlaylistCategoryRepository, Repository)

    @pytest.mark.parametrize(
        "invalid_type, expected", [({}, None), ([], None), ((), None)]
    )
    @patch("flask_sqlalchemy._QueryProperty.__get__")
    def test_get_by_id(
        self, mocked_query_get, app_test, invalid_type, expected
    ):
        dummy = PlaylistCategory()
        dummy.playlist_id = 1
        dummy.category_id = 2
        mocked_query_get.return_value.get.return_value = dummy

        with app_test.app_context():
            first_playlist_category = PlaylistCategoryRepository.get_by_id(1)
            assert isinstance(first_playlist_category, PlaylistCategory)
            assert first_playlist_category.playlist_id == 1
            assert first_playlist_category.category_id == 2

            invalid_playlist_category = PlaylistCategoryRepository.get_by_id(
                invalid_type
            )
            assert invalid_playlist_category is expected
            assert not invalid_playlist_category
