from app.database import db


class Category(db.Model):
    '''
        Categories for playlists
    '''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
