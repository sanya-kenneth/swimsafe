from api.database.db import db
import flask_whooshalchemyplus


class Pool(db.Model):
    __searchable__ = ['pool_name', 'pool_address']
    pool_id = db.Column('pool_id', db.Integer, primary_key=True)
    pool_name = db.Column('pool_name', db.String(80),
                          nullable=False, unique=True)
    pool_address = db.Column('pool_address', db.String(100), nullable=False)
    location_lat = db.Column('location_lat', db.Float, nullable=False)
    location_long = db.Column('location_long', db.Float, nullable=False)
    opening_time = db.Column('opening_time', db.Text, nullable=False)
    closing_time = db.Column('closing_time', db.Text, nullable=False)
    size = db.Column('size', db.Text, nullable=False)
    depth = db.Column('depth', db.Text, nullable=False)
    description = db.Column('description', db.Text, nullable=False)
    weekday_fee = db.Column('weekday_fee', db.Integer, nullable=False)
    weekend_fee = db.Column('weekend_fee', db.Integer, nullable=False)
    available = db.Column('available', db.String(120),
                          default='not available')
    pool_thumbnail = db.Column('pool_thumnail', db.Text, nullable=True)


    def __repr__(self):
        return 'Pool %r' % self.pool_name
