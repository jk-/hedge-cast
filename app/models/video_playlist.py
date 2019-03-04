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
    order_by = db.Column(db.Integer, default=0)
    video = db.relationship(Video, backref=db.backref("video"))
    playlist = db.relationship(Playlist, backref=db.backref("playlist"))
