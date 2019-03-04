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
        assert PlaylistCategoryRepository._isinstance(
            PlaylistCategory(), raise_error=False
        )

    @patch("flask_sqlalchemy._QueryProperty.__get__")
    def test_get(self, mocked_query_get, app_test):
        dummy = PlaylistCategory()
        mocked_query_get.return_value.get.return_value = dummy

        with app_test.app_context():
            first_playlist_category = PlaylistCategoryRepository.get(1)
            assert isinstance(first_playlist_category, PlaylistCategory)
