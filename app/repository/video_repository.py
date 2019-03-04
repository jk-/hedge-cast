from app.models.video import Video
from app.database import Repository


class VideoRepository(Repository):
    __model__ = Video

    @classmethod
    def get_by_search(cls, search_term):
        if isinstance(search_term, str):
            return cls.__model__.query.filter(
                cls.__model__.title.like(search_term + "%")
            ).all()
        return None
