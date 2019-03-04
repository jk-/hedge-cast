from app.models.playlist import Playlist
from app.database import Repository


class PlaylistRepository(Playlist, Repository):
    __name__ = "app.models.playlist.Playlist"
