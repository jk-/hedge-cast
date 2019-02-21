from app.database import db


class PlaylistCategory(db.Model):
    """
        Relational for playlist -> category
    """

    playlist_id = db.Column(
        db.Integer,
        db.ForeignKey("playlist.id", ondelete="CASCADE"),
        primary_key=True,
    )
    category_id = db.Column(
        db.Integer,
        db.ForeignKey("category.id", ondelete="CASCADE"),
        primary_key=True,
    )
