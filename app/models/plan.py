from app.database import db


class Plan(db.Model):
    """
        Subscription plans for users
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    enabled = db.Column(db.Boolean(), default=1)
    code = db.Column(db.String(255), nullable=False)
    interval_term = db.Column(db.String(255), nullable=False)
    interval_count = db.Column(db.Integer, nullable=False, default=1)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    trial_days = db.Column(db.Integer, nullable=False, default=1)
    statement_desc = db.Column(db.String(255), nullable=False)
    plan_group = db.Column(db.String(255), nullable=False)

    def update(self, **kwargs):
        for attr, value in kwargs.items():
            if attr not in ("id",):
                setattr(self, attr, value)
        return self

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            enabled=int(self.enabled),
            code=self.code,
            interval_term=int(self.interval_term),
            interval_count=int(self.interval_count),
            price=float(self.price),
            trial_days=int(self.trial_days),
            statement_desc=self.statement_desc,
            plan_group=self.plan_group,
        )
