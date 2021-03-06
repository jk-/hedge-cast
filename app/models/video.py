import datetime
from app.database import db


class Video(db.Model):
    """
        A video
    """

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    created = db.Column(
        db.DateTime(timezone=True), default=datetime.datetime.utcnow
    )
    access_type = db.Column(db.String(255), nullable=False)
    enabled = db.Column(db.Boolean(), default=0, nullable=False)
    url = db.Column(db.String(255), nullable=False)
    source = db.Column(db.String(255), nullable=False)
    thumbnail = db.Column(db.String(255))

    def update(self, **kwargs):
        for attr, value in kwargs.items():
            if attr not in ("id", "created"):
                setattr(self, attr, value)
        return self

    def to_dict(self):
        return dict(
            id=self.id,
            title=self.title,
            created=self.created.timestamp(),
            access_type=self.access_type,
            enabled=int(self.enabled),
            url=self.url,
            source=self.source,
            thumbnail=self.thumbnail,
        )
