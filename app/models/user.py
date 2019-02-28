import datetime

from app.database import db
from app.extensions import bcrypt
from app.util.serialize import serialize
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import validates


class User(db.Model):
    """
        a user

        TODO:
            The salt key is not unique per user.
            Check set_password and init
    """

    id = db.Column(db.Integer, primary_key=True)
    _username = db.Column(
        "username", db.String(20), nullable=False, unique=True
    )
    _username_canonical = db.Column(
        "username_cononical", db.String(20), nullable=False, unique=True
    )
    _email = db.Column("email", db.String(180), nullable=False, unique=True)
    _email_canonical = db.Column(
        "email_canonical", db.String(180), nullable=False, unique=True
    )
    _email_reverse = db.Column(
        "email_reverse", db.String(180), nullable=False, unique=True
    )
    enabled = db.Column(db.Boolean(), default=1, nullable=False)
    _salt = db.Column("salt", db.String(255), nullable=False)
    _password = db.Column("password", db.String(255), nullable=False)
    last_login_at = db.Column(
        db.DateTime(timezone=True), default=datetime.datetime.utcnow
    )
    referrer = db.Column(db.String(255))
    locked = db.Column(db.Boolean(), default=0)
    confirmation_token = db.Column(db.String(255))
    password_requested_at = db.Column(db.DateTime(timezone=True))
    roles = db.relationship("Role", secondary="user_roles", lazy="joined")
    plans = db.relationship("Plan", secondary="user_plan", lazy="joined")
    credentials_expire_at = db.Column(db.DateTime(timezone=True))
    _created = db.Column(
        "created", db.DateTime(timezone=True), default=datetime.datetime.utcnow
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
                "last_login_at",
                "roles",
                "plans",
            ):
                setattr(self, attr, value)
        return self

    @hybrid_property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username
        self._username_canonical = username

    @hybrid_property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email
        self._email_canonical = email
        self._email_reverse = email[::-1]

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self.set_password(password)

    @hybrid_property
    def created(self):
        return self._created

    def set_password(self, password):
        hash_ = bcrypt.generate_password_hash(password, 10).decode("utf-8")
        self._password = hash_
        self._salt = "asdf"

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
            roles=[serialize(x) for x in self.roles],
            plans=[serialize(x) for x in self.plans],
        )
