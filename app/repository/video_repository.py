from app.models.video import Video
from app.database import Repository


class VideoRepository(Repository):
    __model__ = Video

    def get_by_search(search_term):
        if isinstance(search_term, str):
            return self.__model__.query.filter(
                self.__model__.title.like(search_term + "%")
            ).all()
        return None
