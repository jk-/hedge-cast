from app.models.video_playlist import VideoPlaylist
from app.database import Repository


class VideoPlaylistRepository(Repository):
    __model__ = VideoPlaylist
