from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField
from wtforms.validators import DataRequired, Length


class PlanValidator(FlaskForm):
    name = StringField(
        "name", validators=[DataRequired(), Length(min=2, max=32)]
    )
    code = StringField(
        "code", validators=[DataRequired(), Length(min=3, max=16)]
    )
    interval_term = IntegerField("interval_term", validators=[DataRequired()])
    interval_count = IntegerField(
        "interval_count", validators=[DataRequired()]
    )
    price = DecimalField("price", validators=[DataRequired()])
    trial_days = IntegerField("trial_days")
    statement_desc = StringField(
        "statement_desc", validators=[DataRequired(), Length(min=3, max=16)]
    )
    plan_group = StringField(
        "plan_group", validators=[DataRequired(), Length(min=3, max=16)]
    )
