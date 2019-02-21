from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_

db = SQLAlchemy()


class Repository:
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

    @staticmethod
    def save(entity, commit=True):
        db.session.add(entity)
        if commit:
            db.session.commit()
        return entity

    @staticmethod
    def delete(entity, ommit=True):
        db.session.delete(entity)
        return commit and db.session.commit()
