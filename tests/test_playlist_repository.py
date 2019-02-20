import pytest

from app.models.playlist import Playlist
from app.database import Repository
from app.repository.playlist_repository import PlaylistRepository
from unittest.mock import patch


class TestPlaylistRepository:
    @pytest.mark.smoke
    def test_init(self):
        assert issubclass(PlaylistRepository, Playlist)
        assert issubclass(PlaylistRepository, Repository)

    @pytest.mark.parametrize(
        "invalid_type, expected", [({}, None), ([], None), ((), None)]
    )
    @patch("flask_sqlalchemy._QueryProperty.__get__")
    def test_get_by_id(
        self, mocked_query_get, app_test, invalid_type, expected
    ):
        dummy = Playlist()
        dummy.name = "Playlist Name"
        mocked_query_get.return_value.get.return_value = dummy

        with app_test.app_context():
            first_playlist = PlaylistRepository.get_by_id(1)
            assert isinstance(first_playlist, Playlist)
            assert first_playlist.name == "Playlist Name"
            assert not first_playlist.name == "Balls"

            invalid_playlist = PlaylistRepository.get_by_id(invalid_type)
            assert invalid_playlist is expected
            assert not invalid_playlist
