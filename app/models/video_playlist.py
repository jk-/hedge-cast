from app.database import db


class VideoPlaylist(db.Model):
    """
        Relational video -> playlist
    """

    video_is = db.Column(
        db.Integer, db.ForeignKey("video.id"), primary_key=True
    )
    playlist_id = db.Column(
        db.Integer, db.ForeignKey("playlist.id"), primary_key=True
    )
