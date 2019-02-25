from app.database import db


class Category(db.Model):
    """
        Categories for videos / playlists
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    def to_dict(self):
        return dict(id=self.id, name=self.name)

    def update(self, **kwargs):
        for attr, value in kwargs.items():
            if attr not in ("id",):
                setattr(self, attr, value)
        return self
