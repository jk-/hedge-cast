from app.database import db


class UserPlan(db.Model):
    """
        relational of user -> plan
    """

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id", ondelete="CASCADE"),
        primary_key=True,
    )
    plan_id = db.Column(
        db.Integer,
        db.ForeignKey("plan.id", ondelete="CASCADE"),
        primary_key=True,
    )
