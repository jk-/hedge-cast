from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class PlanValidator(FlaskForm):
    name = StringField(
        "name", validators=[DataRequired(), Length(min=2, max=32)]
    )
    code = StringField(
        "code", validators=[DataRequired(), Length(min=3, max=16)]
    )

    # interval_term =
    # interval_count =
    # price =
    # trial_days =
    # statement_desc =
    # plan_group =
