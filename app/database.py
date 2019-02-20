from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_

db = SQLAlchemy()


class Repository(object):
    """
    This does not track dirty values - will update
    entire object!
    """

    @classmethod
    def get_by_id(cls, id):
        if any(
            (
                isinstance(id, str) and id.isdigit(),
                isinstance(id, (int, float)),
            )
        ):
            return cls.query.get(int(id))
        return None

    def update(self, commit=True, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        return commit and self.save() or self

    def save(self, commit=True):
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def delete(self, commit=True):
        db.session.delete(self)
        return commit and db.session.commit()
