from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, DateTimeField
from wtforms.validators import DataRequired, Length


class VideoValidator(FlaskForm):
    title = StringField(
        "title", validators=[DataRequired(), Length(min=2, max=32)]
    )
    created = DateTimeField("created")
    access_type = StringField(
        "access_type", validators=[DataRequired(), Length(min=2, max=32)]
    )
    enabled = BooleanField("enabled")
    url = StringField(
        "url", validators=[DataRequired(), Length(min=15, max=128)]
    )
    source = StringField(
        "source", validators=[DataRequired(), Length(min=5, max=128)]
    )
    thumbnail = StringField(
        "thumbnail", validators=[DataRequired(), Length(min=5, max=128)]
    )
