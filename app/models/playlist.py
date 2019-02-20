from app.database import db


class Playlist(db.Model):
    '''
        Playlists (list) of video objects
    '''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    category_id = db.Column(
        db.Integer,
        db.ForeignKey('category.id'),
        nullable=False
    )
    enabled = None
