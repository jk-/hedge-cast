import datetime

from flask_login import UserMixin
from app.database import db, CRUDMixin


class User(CRUDMixin, db.Model):
    '''
        a user

        TODO:
            The salt key is not unique per user.
            Check set_password and init
    '''
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    username_canonical = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(180), nullable=False, unique=True)
    email_canonical = db.Column(db.String(180), nullable=False, unique=True)
    email_reserved = db.Column(db.String(180), nullable=False, unique=True)
    enabled = db.Column(db.Boolean(), default=1)
    salt = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    last_login_at = db.Column(
        db.DateTime(timezone=True),
        default=datetime.datetime.utcnow
    )
    referrer = db.Column(db.String(255))
    locked = db.Column(db.Boolean(), default=0)
    confirmation_token = db.Column(db.String(255))
    password_requested_at = db.Column(db.DateTime(timezone=True))
    # this wont work because if we have multiple roles
    # then we can extend past the varchar 255
    roles = db.Column(db.String(255))
    credentials_expire_at = db.Column(
        db.DateTime(timezone=True)
    )
    created = db.Column(
        db.DateTime(timezone=True),
        default=datetime.datetime.utcnow
    )
    stripe_customer_id = db.Column(db.String(255))
    can_email_notify = db.Column(db.Boolean(), default=1)
    can_email_general = db.Column(db.Boolean(), default=1)

    def __init__(self, password, **kwargs):
        super(User, self).__init__(**kwargs)
        self.set_password(password)

    def __repr__(self):
        return '<User #%s:%r>' % (self.id, self.username)

    def set_password(self, password):
        hash_ = bcrypt.generate_password_hash(password, 10).decode('utf-8')
        self.password = hash_

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)
