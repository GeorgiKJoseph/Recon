from flask import render_template, redirect, url_for, abort, request, json
from flask_login import UserMixin

from app import db, login_manager

from app.iot_integration import blueprint

from app.base.models import(
    VehicleSight,
    VehicleRegistration,
    Camera,
    Blacklist
)

SECRET_KEY = 'Xn2r5u8x/A?D(G-KaPdS'
directions = ['north', 'south', 'east', 'west']


# Ping_handle for Iot
# Hail cutie for access token
@blueprint.route('/iot/ping', methods=['POST'])
def iot_ping():
    token = request.form.get('token')
    if token == 'long live cutie':

        # Collecting blacklist
        blacklist = Blacklist.query.all()
        blacklist = [x.vehicle_id for x in blacklist]

        return json.dumps({
            'status':'OK',
            'access_token': SECRET_KEY,
            'blacklist': blacklist
            })
    return json.dumps({'status':'ERROR'})


# Update status on vehicle sight
@blueprint.route('/iot/sight', methods=['POST'])
def register_sight():
    token = request.form.get('access_token')
    if token == SECRET_KEY:
        cam_id = request.form.get('cam_id')
        vehicle_id = request.form.get('vehicle_id')
        direction = request.form.get('direction')
        if direction not in directions:
            direction = ''
        cam = Camera.query.filter_by(id=cam_id).first()
        vehicle = VehicleRegistration.query.filter_by(id=vehicle_id).first()
        if cam != None and vehicle != None:
            sight = VehicleSight(
                vehicle_number = vehicle_id,
                latitude = cam.latitude,
                longitude = cam.longitude,
                place = cam.place,
                direction = direction,
                camera_id = cam_id
            )
            db.session.add(sight)
            db.session.commit()
            return json.dumps({'status':'OK'})
    return json.dumps({'status':'ERROR'})
