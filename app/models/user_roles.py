from app.database import db


class UserRoles(db.Model):
    __tablename__ = "user_roles"
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(
        db.Integer(), db.ForeignKey("user.id", ondelete="CASCADE")
    )
    role_id = db.Column(
        db.Integer(), db.ForeignKey("roles.id", ondelete="CASCADE")
    )
