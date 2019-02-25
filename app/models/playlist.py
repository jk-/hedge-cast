from app.database import db


class Playlist(db.Model):
    """
        Playlists (list) of video objects
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    category_id = db.Column(
        db.Integer, db.ForeignKey("category.id"), nullable=False
    )
    enabled = db.Column(db.Boolean(), default=1)

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            category_id=self.category_id,
            enabled=self.enabled,
        )
