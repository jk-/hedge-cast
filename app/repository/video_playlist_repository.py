from app.models.video_playlist import VideoPlaylist
from app.database import Repository


class VideoPlaylistRepository(VideoPlaylist, Repository):
    pass
