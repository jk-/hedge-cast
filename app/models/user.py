import datetime

from app.database import db
from app.extensions import bcrypt


class User(db.Model):
    """
        a user

        TODO:
            The salt key is not unique per user.
            Check set_password and init
    """

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    username_canonical = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(180), nullable=False, unique=True)
    email_canonical = db.Column(db.String(180), nullable=False, unique=True)
    email_reverse = db.Column(db.String(180), nullable=False, unique=True)
    enabled = db.Column(db.Boolean(), default=1)
    salt = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    last_login_at = db.Column(
        db.DateTime(timezone=True), default=datetime.datetime.utcnow
    )
    referrer = db.Column(db.String(255))
    locked = db.Column(db.Boolean(), default=0)
    confirmation_token = db.Column(db.String(255))
    password_requested_at = db.Column(db.DateTime(timezone=True))
    roles = db.relationship("Role", secondary="user_roles")
    credentials_expire_at = db.Column(db.DateTime(timezone=True))
    created = db.Column(
        db.DateTime(timezone=True), default=datetime.datetime.utcnow
    )
    stripe_customer_id = db.Column(db.String(255))
    can_email_notify = db.Column(db.Boolean(), default=1)
    can_email_general = db.Column(db.Boolean(), default=1)

    def __repr__(self):
        return "<User #%s:%r>" % (self.id, self.username)

    def update(self, **kwargs):
        for attr, value in kwargs.items():
            if attr not in (
                "id",
                "created",
                "email_canonical",
                "username_canonical",
                "salt",
                "last_login_at",
            ):
                set_method = f"set_{attr}"
                if hasattr(self.__class__, set_method) and callable(
                    getattr(self.__class__, set_method)
                ):
                    getattr(self, set_method)(value)
                else:
                    setattr(self, attr, value)
        return self

    def set_username(self, username):
        setattr(self, "username", username)
        setattr(self, "username_canonical", username)

    def set_last_login_at(self, last_login_at):
        setattr(self, "last_login_at", datetime.datetime.utcnow())

    def set_email(self, email):
        self.email = email
        self.email_canonical = email
        self.email_reverse = email[::-1]

    def set_password(self, password):
        hash_ = bcrypt.generate_password_hash(password, 10).decode("utf-8")
        self.password = hash_
        self.salt = "asdf"

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    def has_roles(self, *args):
        return set(args).issubset({role.name for role in self.roles})

    def to_dict(self):
        return dict(
            id=self.id,
            username=self.username,
            created=int(self.created.timestamp()),
            enabled=int(self.enabled),
            email=self.email,
            last_login_at=self.last_login_at,
            can_email_notify=self.can_email_notify,
            can_email_general=self.can_email_general,
            stripe_customer_id=self.stripe_customer_id,
        )
