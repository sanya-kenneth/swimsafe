from api.database.db import db


class Pool(db.Model):
    pool_id = db.Column('pool_id', db.Integer, primary_key=True)
    pool_name = db.Column('name', db.String(80), nullable=False, unique=True)
    pool_address = db.Column('address', db.String(100), nullable=False)
    location_lat = db.Column('location_lat', db.Float, nullable=False)
    location_long = db.Column('location_long', db.Float, nullable=False)
    opening_time = db.Column('opening_time', db.Text, nullable=False)
    closing_time = db.Column('closing_time', db.Text, nullable=False)
    size = db.Column('size', db.Text, nullable=False)
    depth = db.Column('depth', db.Text, nullable=False)
    images = db.Column('images', db.ARRAY(db.Text), nullable=True)
    description = db.Column('description', db.Text, nullable=False)
    cost = db.Column('cost', db.Integer, nullable=False)
    available = db.Column('available', db.String(120),
                          default='not available')


    def __repr__(self):
        return 'Pool %r' % self.pool_name
