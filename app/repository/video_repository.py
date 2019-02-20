from app.models.video import Video
from app.database import Repository


class VideoRepository(Video, Repository):
    pass
