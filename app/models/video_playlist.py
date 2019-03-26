from app.database import db
from app.models.video import Video
from app.models.playlist import Playlist


class VideoPlaylist(db.Model):
    """
        Relational video -> playlist
    """

    video_id = db.Column(
        db.Integer,
        db.ForeignKey("video.id", ondelete="CASCADE"),
        primary_key=True,
    )
    playlist_id = db.Column(
        db.Integer,
        db.ForeignKey("playlist.id", ondelete="CASCADE"),
        primary_key=True,
    )
    order = db.Column(db.Integer, default=0)
    video = db.relationship(Video)
    playlist = db.relationship(Playlist)
