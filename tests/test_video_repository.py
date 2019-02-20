import pytest

from app.models.video import Video
from app.database import Repository
from app.repository.video_repository import VideoRepository
from unittest.mock import patch


class TestVideoRepository:
    @pytest.mark.smoke
    def test_init(self):
        assert issubclass(VideoRepository, Video)
        assert issubclass(VideoRepository, Repository)

    @pytest.mark.parametrize(
        "invalid_type, expected", [({}, None), ([], None), ((), None)]
    )
    @patch("flask_sqlalchemy._QueryProperty.__get__")
    def test_get_by_id(
        self, mocked_query_get, app_test, invalid_type, expected
    ):
        dummy = Video()
        dummy.id = 1
        dummy.title = "jon"
        mocked_query_get.return_value.get.return_value = dummy

        with app_test.app_context():
            first_video = VideoRepository.get_by_id(1)
            assert isinstance(first_video, Video)
            assert first_video.id == 1
            assert first_video.title == "jon"
            assert not first_video.title == "josh"

            invalid_video = VideoRepository.get_by_id(invalid_type)
            assert invalid_video is expected
            assert not invalid_video
