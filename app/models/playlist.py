from app.database import db
from app.util.serialize import serialize


class Playlist(db.Model):
    """
        Playlists (list) of video objects
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    enabled = db.Column(db.Boolean(), default=0)
    categories = db.relationship(
        "Category", secondary="playlist_category", lazy="dynamic"
    )
    videos = db.relationship(
        "Video",
        secondary="video_playlist",
        lazy="dynamic",
        order_by="VideoPlaylist.order",
    )

    def update(self, **kwargs):
        for attr, value in kwargs.items():
            if attr not in ("id", "categories", "videos"):
                setattr(self, attr, value)
        return self

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            enabled=self.enabled,
            categories=[serialize(x) for x in self.categories],
            videos=[serialize(x) for x in self.videos],
        )
