from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_

db = SQLAlchemy()


class Repository:
    """
    This does not track dirty values - will update
    entire object!
    """

    @classmethod
    def get(cls, id):
        if any(
            (
                isinstance(id, str) and id.isdigit(),
                isinstance(id, (int, float)),
            )
        ):
            return cls.query.get(int(id))
        return None

    @staticmethod
    def save(entity, commit=True):
        db.session.add(entity)
        if commit:
            db.session.commit()
        return entity

    @staticmethod
    def delete(entity, commit=True):
        db.session.delete(entity)
        return commit and db.session.commit()
