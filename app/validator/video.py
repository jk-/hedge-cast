from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, DateTimeField
from wtforms.validators import DataRequired, Length


class VideoValidator(FlaskForm):
    title = StringField("title", validators=[DataRequired(), Length(max=32)])
    access_type = StringField(
        "access_type", validators=[DataRequired(), Length(max=32)]
    )
    enabled = BooleanField("enabled")
    url = StringField("url", validators=[DataRequired(), Length(max=128)])
    source = StringField(
        "source", validators=[DataRequired(), Length(max=128)]
    )
    thumbnail = StringField(
        "thumbnail", validators=[DataRequired(), Length(max=128)]
    )
