from app.database import db


class Category(db.Model):
    """
        Categories for videos / playlists
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    def to_dict(self):
        return dict(id=self.id, name=self.name)
