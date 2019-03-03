from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class RoleValidator(FlaskForm):
    name = StringField(
        "name", validators=[DataRequired(), Length(min=5, max=32)]
    )
