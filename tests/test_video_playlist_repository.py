import pytest

from app.models.video_playlist import VideoPlaylist
from app.database import Repository
from app.repository.video_playlist_repository import VideoPlaylistRepository
from unittest.mock import patch


class TestVideoPlaylistRepository:
    @pytest.mark.smoke
    def test_init(self):
        assert VideoPlaylistRepository._isinstance(
            VideoPlaylist(), raise_error=False
        )

    @patch("flask_sqlalchemy._QueryProperty.__get__")
    def test_get(self, mocked_query_get, app_test):
        dummy = VideoPlaylist()
        mocked_query_get.return_value.get.return_value = dummy

        with app_test.app_context():
            first_video_playlist = VideoPlaylistRepository.get(1)
            assert isinstance(first_video_playlist, VideoPlaylist)
