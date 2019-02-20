from app.models.playlist_category import PlaylistCategory
from app.database import Repository


class PlaylistCategoryRepository(PlaylistCategory, Repository):
    pass
