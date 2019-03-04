import pytest

from app.models.video import Video
from app.database import Repository
from app.repository.video_repository import VideoRepository
from unittest.mock import patch


class TestVideoRepository:
    @pytest.mark.smoke
    def test_init(self):
        assert VideoRepository._isinstance(Video(), raise_error=False)

    @patch("flask_sqlalchemy._QueryProperty.__get__")
    def test_get(self, mocked_query_get, app_test):
        dummy = Video()
        mocked_query_get.return_value.get.return_value = dummy

        with app_test.app_context():
            first_video = VideoRepository.get(1)
            assert isinstance(first_video, Video)
