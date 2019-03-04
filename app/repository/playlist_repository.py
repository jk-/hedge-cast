from app.models.playlist import Playlist
from app.database import Repository


class PlaylistRepository(Repository):
    __model__ = Playlist
