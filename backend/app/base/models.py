from flask_login import UserMixin
from sqlalchemy import (
    BINARY,
    Column,
    Integer,
    String,
    Boolean,
    Float,
    ForeignKey,
    BigInteger,
    TIMESTAMP,
    func
)
from app import db, login_manager


class VehicleSight(db.Model):
    __tablename__ = 'recon_vehicle_sight'

    id = Column(Integer, primary_key=True)
    time = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    vehicle_number = Column(String, ForeignKey('recon_vehicle_registration.id'))
    latitude = Column(String)
    longitude = Column(String)
    place = Column(String)
    direction = Column(String)
    camera_id = Column(Integer, ForeignKey('recon_camera.id'))

    def __repr__(self):
        return '<VehicleSight:{}>'.format(self.vehicle_number)


class VehicleRegistration(db.Model):
    __tablename__ = 'recon_vehicle_registration'

    id = Column(String, primary_key=True)
    owner = Column(String)
    vehicle_type = Column(String)
    brand = Column(String)
    model = Column(String)
    color = Column(String)
    def __repr__(self):
        return '<VehicleRegistration:{},{}>'.format(self.id, self.model)


class Camera(db.Model):
    __tablename__ = 'recon_camera'

    id = Column(Integer, primary_key=True)
    cam_type = Column(String)
    latitude = Column(String)
    longitude = Column(String)
    place = Column(String)
    description = Column(String)
    mobile_unit_id = Column(String)

    def __repr__(self):
        return '<Camera:{}>'.format(self.id)


class Blacklist(db.Model):
    __tablename__ = 'recon_blacklist'

    id = Column(Integer, primary_key=True)
    vehicle_id = Column(Integer, ForeignKey('recon_vehicle_registration.id'))
    last_seen_time = Column(TIMESTAMP)
    last_seen_place = Column(String)
    latitude = Column(String)
    longitude = Column(String)

    def __repr__(self):
        return '<Blacklist:{}>'.format(self.vehicle_id)


# class Blacklist_hits(db.Model):
#     __tablename__ = 'recon_blacklist_hit'

#     id = Column(Integer, primary_key=True)
#     blacklist_id = Column(Integer, ForeignKey('recon_blacklist.id'))
#     vehicle_id = Column(Integer, ForeignKey('recon_vehicle_registration.id'))
#     sight_id = Column(Integer, ForeignKey('recon_vehicle_sight.id'))
#     time = Column(TIMESTAMP)

#     def __repr__(self):
#         return '<Blacklist_hits:{}>'.format(self.vehicle_id)

