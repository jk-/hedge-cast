import pytest

from app.models.video_playlist import VideoPlaylist
from app.database import Repository
from app.repository.video_playlist_repository import VideoPlaylistRepository
from unittest.mock import patch


class TestVideoPlaylistRepository:
    @pytest.mark.smoke
    def test_init(self):
        assert issubclass(VideoPlaylistRepository, VideoPlaylist)
        assert issubclass(VideoPlaylistRepository, Repository)

    @pytest.mark.parametrize(
        "invalid_type, expected", [({}, None), ([], None), ((), None)]
    )
    @patch("flask_sqlalchemy._QueryProperty.__get__")
    def test_get_by_id(
        self, mocked_query_get, app_test, invalid_type, expected
    ):
        dummy = VideoPlaylist()
        dummy.video_id = 1
        dummy.playlist_id = 2
        mocked_query_get.return_value.get.return_value = dummy

        with app_test.app_context():
            first_video_playlist = VideoPlaylistRepository.get_by_id(1)
            assert isinstance(first_video_playlist, VideoPlaylist)
            assert first_video_playlist.video_id == 1
            assert first_video_playlist.playlist_id == 2

            invalid_video_playlist = VideoPlaylistRepository.get_by_id(
                invalid_type
            )
            assert invalid_video_playlist is expected
            assert not invalid_video_playlist
