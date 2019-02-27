from app.database import db


class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

    def update(self, **kwargs):
        for attr, value in kwargs.items():
            if attr not in ("id",):
                setattr(self, attr, value)
        return self

    def to_dict(self):
        return dict(id=self.id, name=self.name)
