from app.database import db


class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)

    def to_dict(self):
        return dict(id=self.id, name=self.name)
