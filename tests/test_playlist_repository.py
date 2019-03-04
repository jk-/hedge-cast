import pytest

from app.models.playlist import Playlist
from app.database import Repository
from app.repository.playlist_repository import PlaylistRepository
from unittest.mock import patch


class TestPlaylistRepository:
    @pytest.mark.smoke
    def test_init(self):
        assert PlaylistRepository._isinstance(Playlist(), raise_error=False)

    @patch("flask_sqlalchemy._QueryProperty.__get__")
    def test_get(self, mocked_query_get, app_test):
        dummy = Playlist()
        mocked_query_get.return_value.get.return_value = dummy

        with app_test.app_context():
            first_playlist = PlaylistRepository.get(1)
            assert isinstance(first_playlist, Playlist)
