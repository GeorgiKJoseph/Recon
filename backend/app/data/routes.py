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


# Ping_handle for Data entry
# Hail cutie for access token
@blueprint.route('/data/ping', methods=['POST'])
def data_ping():
    token = request.form.get('token')
    if token == 'long live cutie':
        return json.dumps({
            'status':'OK',
            'access_token': SECRET_KEY,
            })
    return json.dumps({'status':'ERROR'})


# Add Vehicle data
@blueprint.route('/data/vehicle', methods=['POST'])
def data_vehicle():
    token = request.form.get('access_token')
    if token == SECRET_KEY:
        id = request.form.get('vehicle_no')
        owner = request.form.get('owner')
        vehicle_type = request.form.get('vehicle_type')
        brand = request.form.get('brand')
        model = request.form.get('model')
        color = request.form.get('color')
        vehicle = VehicleRegistration.query.filter_by(id=id).first()
        if vehicle == None:
            new_vehicle = VehicleRegistration(
                id = id,
                owner = owner,
                vehicle_type = vehicle_type,
                brand = brand,
                model = model,
                color = color
            )
            db.session.add(new_vehicle)
            db.session.commit()
            return json.dumps({'status':'OK'})
        else:
            return json.dumps({
                'status':'OK',
                'msg':'{} already exists.'.format(id)
            })
    return json.dumps({'status':'ERROR 403'})


# Add cam data
@blueprint.route('/data/cam', methods=['POST'])
def data_cam():
    token = request.form.get('access_token')
    if token == SECRET_KEY:
        cam_type = request.form.get('cam_type')
        latitude = request.form.get('latitude')
        longitude = request.form.get('longitude')
        place = request.form.get('place')
        description = request.form.get('description')
        cam = Camera.query.filter_by(latitude=latitude).filter_by(longitude=longitude).first()
        if cam == None:
            new_cam = Camera(
                cam_type = cam_type,
                latitude = latitude,
                longitude = longitude,
                place = place,
                description = description
            )
            db.session.add(new_cam)
            db.session.commit()
            return json.dumps({'status':'OK'})
        else:
            return json.dumps({
                'status':'OK',
                'msg':'Cam already exists.'
            })
    return json.dumps({'status':'ERROR 403'})

