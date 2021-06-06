from flask_wtf import FlaskForm

from wtforms.validators import DataRequired
from wtforms.fields.html5 import(
    SearchField
)

class TrackForm(FlaskForm):
    vehicle_id = SearchField('Vehicle number', id='vehicle_id', validators=[DataRequired()])