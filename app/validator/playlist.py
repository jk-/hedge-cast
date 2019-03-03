from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired, Length


class PlaylistValidator(FlaskForm):
    name = StringField(
        "name", validators=[DataRequired(), Length(min=3, max=32)]
    )
    enabled = BooleanField("enabled")
