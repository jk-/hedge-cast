from app.database import db


class PlaylistCategory(db.Model):
    '''
        Relational for playlist -> category
    '''
    playlist_id = db.Column(
        db.Integer,
        db.ForeignKey('playlist.id'),
        primary_key=True
    )
    category_id = db.Column(
        db.Integer,
        db.ForeignKey('category.id'),
        primary_key=True
    )
