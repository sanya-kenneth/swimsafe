from api.database.db import db


class Children_Pool(db.Model):
    child_pool_id = db.Column('child_pool_id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(80),
                          nullable=False, unique=True)
    size = db.Column('size', db.Text, nullable=False)
    depth = db.Column('depth', db.Text, nullable=False)
    description = db.Column('description', db.Text, nullable=False)
    weekday_fee = db.Column('weekday_fee', db.Integer, nullable=False)
    weekend_fee = db.Column('weekend_fee', db.Integer, nullable=False)
    available = db.Column('available', db.String(120),
                          default='not available')
    pool_id = db.Column(db.Integer, db.ForeignKey('pool.pool_id'),
                        nullable=False)
    thumbnail = db.Column('thumnail', db.Text, nullable=True)


    def __repr__(self):
        return self.name
