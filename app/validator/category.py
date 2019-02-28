from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class CategoryValidator(FlaskForm):
    name = StringField(
        "name", validators=[DataRequired(), Length(min=2, max=32)]
    )
