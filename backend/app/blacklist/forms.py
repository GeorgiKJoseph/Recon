from flask_wtf import FlaskForm

from wtforms.validators import DataRequired
from wtforms.fields.html5 import(
    SearchField,
    DateTimeField
)

class MissingForm(FlaskForm):
    vehicle_id = SearchField('Vehicle number', id='vehicle_id', validators=[DataRequired()])
    time = DateTimeField('Last seen', id='time', validators=[DataRequired()])
    place = SearchField('Place', id='place', validators=[DataRequired()])
    latitude = SearchField('Vehicle number', id='vehicle_id', validators=[DataRequired()])
    longitude = SearchField('Vehicle number', id='vehicle_id', validators=[DataRequired()])