from app.models.video import Video
from app.database import Repository


class VideoRepository(Video, Repository):
    @staticmethod
    def get_by_search(search_term):
        if isinstance(search_term, str):
            return Video.query.filter(
                Video.title.like(search_term + "%")
            ).all()
        return None
