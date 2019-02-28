from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email, Length


class UserValidator(FlaskForm):
    username = StringField(
        "username", validators=[DataRequired(), Length(min=2, max=24)]
    )
    email = StringField(
        "email", validators=[DataRequired(), Email(), Length(max=128)]
    )


class UserRegistrationValidator(UserValidator):
    pass
