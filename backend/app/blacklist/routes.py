from flask import render_template, redirect, url_for, abort, request
from flask_login import UserMixin

from app import db, login_manager

from app.blacklist import blueprint
from app.blacklist.forms import MissingForm

from app.base.models import(
    VehicleSight,
    VehicleRegistration,
    Camera,
    Blacklist
)

from datetime import datetime


@blueprint.route('/report/missing', methods=['GET', 'POST'])
def report_missing():
    missingForm = MissingForm(request.form)
    if request.method == "POST":
        vehicle_id = request.form['vehicle_id'].upper()
        missing_vehicle = Blacklist.query.filter_by(vehicle_id=vehicle_id).first()
        vehicle_reg = VehicleRegistration.query.filter_by(id=vehicle_id).first()
        if missing_vehicle != None:
            return render_template(
                'report_missing.html',
                missingForm=missingForm,
                msg = 'Vehicle already exists in blacklist.'
            )
        elif vehicle_reg == None:
            return render_template(
                'report_missing.html',
                missingForm=missingForm,
                msg = 'Vehicle does not exists.'
            )
        else:
            try:
                time_in = request.form['time']
                time_final = datetime(
                    int(time_in[:4]), int(time_in[5:7]),
                    int(time_in[8:10]), int(time_in[11:13]),
                    int(time_in[14:16])
                )
                new_missing = Blacklist(
                    vehicle_id = vehicle_id,
                    last_seen_time = datetime.now(),
                    last_seen_place = request.form['place'],
                    latitude = request.form['latitude'],
                    longitude = request.form['longitude'],
                )
                db.session.add(new_missing)
                db.session.commit()
            except:
                db.session.rollback()
                return render_template(
                    'report_missing.html',
                    missingForm=missingForm,
                    msg = 'Entry failed, Try again'
                )
            return redirect(url_for('blacklist_blueprint.list_blacklist'))

    return render_template('report_missing.html', missingForm=missingForm)


@blueprint.route('/blacklist', methods=['GET', 'POST'])
def list_blacklist():
    blacklist = Blacklist.query.all()
    return render_template('blacklist.html', blacklist=blacklist)
