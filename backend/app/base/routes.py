from flask import render_template, redirect, url_for, abort
from flask_login import UserMixin

from app import db, login_manager
from app.base import blueprint

from app.base.models import(
    VehicleSight,
    VehicleRegistration,
    Camera
)
from app.base.utils import(
    getMapCenter
)

@blueprint.route('/')
def route_default():
    return render_template('index.html')


@blueprint.route('/<template>')
def send_template(template):
    return render_template(template)

@login_manager.user_loader
def load_user(id):
    return id

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

# @blueprint.route('/data')
# def data_entry():
#     # reg = VehicleRegistration(
#     #     id = 'KL30F3000',
#     #     owner = 'John Doe',
#     #     vehicle_type = 'sedan',
#     #     brand = 'Honda',
#     #     model = 'Amaze',
#     #     color = 'Black'
#     # )
#     # db.session.add(reg)
#     # cam1 = Camera(
#     #     id = 1,
#     #     cam_type = 'static',
#     #     latitude = '9.318254',
#     #     longitude = '76.614030',
#     #     place = 'Chengannur Bethel Junction',
#     #     description = 'Near KSRTC, Depot, Chengannur',
#     #     mobile_unit_id = ''
#     # )
#     # db.session.add(cam1)
#     sight1 = VehicleSight(
#         id = 1,
#         vehicle_number = 'KL30F3000',
#         latitude = '9.152967',
#         longitude = '76.735611',
#         place = 'Central Junction Adoor',
#         direction = 'North',
#         camera_id = '4'
#     )
#     db.session.add(sight1)

#     sight2 = VehicleSight(
#         id = 2,
#         vehicle_number = 'KL30F3000',
#         latitude = '9.318254',
#         longitude = '76.614030',
#         place = 'Chengannur Bethel Junction',
#         direction = 'North',
#         camera_id = '1'
#     )
#     db.session.add(sight2)

#     sight3 = VehicleSight(
#         id = 3,
#         vehicle_number = 'KL30F3000',
#         latitude = '9.591567',
#         longitude = '76.522156',
#         place = 'JV Kottayam',
#         direction = 'North',
#         camera_id = '3'
#     )
#     db.session.add(sight3)

#     sight4 = VehicleSight(
#         id = 4,
#         vehicle_number = 'KL30F3000',
#         latitude = '9.931233',
#         longitude = '76.267303',
#         place = 'FW Kochi',
#         direction = 'North',
#         camera_id = '2'
#     )
#     db.session.add(sight4)

#     db.session.commit()
#     return 'Done'