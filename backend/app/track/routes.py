from flask import render_template, redirect, url_for, abort, request
from flask_login import UserMixin

from app import db, login_manager

from app.track import blueprint
from app.track.forms import TrackForm

from app.base.models import(
    VehicleSight,
    VehicleRegistration,
    Camera
)
from app.base.utils import(
    getMapCenter
)

@blueprint.route('/track', methods=['GET', 'POST'])
def track_home():
    trackForm = TrackForm(request.form)
    if request.method == 'POST':
        vehicle_no = request.form['vehicle_id']
        vehicle_no = vehicle_no.upper()
        print(vehicle_no)
        info = VehicleRegistration.query.filter_by(id=vehicle_no).first()
        if info == None:
            abort(404)
        else:
            return redirect(url_for('track_blueprint.track_vehicle', vehicle_no=vehicle_no))

    return render_template(
        'track_input.html',
        trackForm = trackForm
    )

@blueprint.route('/track/<vehicle_no>')
def track_vehicle(vehicle_no):
    vehicle_no = vehicle_no.upper()

    # Check registration
    vehicle_info = VehicleRegistration.query.filter_by(id=vehicle_no).first()
    if vehicle_info != None:
        sights = VehicleSight.query.filter_by(vehicle_number=vehicle_no).limit(5).all()
        info = VehicleRegistration.query.filter_by(id=vehicle_no).first()
        center_lat, center_lon = getMapCenter(sights)
        return render_template(
            'track_vehicle.html',
            sights=sights,
            info=info,
            center_lat=center_lat,
            center_lon=center_lon
        )

    abort(404)

# Error handlers
@login_manager.unauthorized_handler
def unauthorized_handler():
    return render_template('page-403.html'), 403

@blueprint.errorhandler(403)
def access_forbidden(error):
    return render_template('page-403.html'), 403

@blueprint.errorhandler(404)
def not_found_error(error):
    return render_template('page-404.html'), 404

@blueprint.errorhandler(500)
def internal_error(error):
    return render_template('page-500.html'), 500
