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


class Pool_packages(db.Model):
    """
    class for creating  a pool package
    args:
        pool_id: the id of the pool to which the package belongs
        package_type: the type of package
        package_details: details for the pool package
    """
    package_id = db.Column('package_id', db.Integer, primary_key=True)
    pool_id = db.Column(db.Integer, db.ForeignKey('pool.pool_id', ondelete='CASCADE'),
                        nullable=False)
    package_type = db.Column('package_type', db.String(120), default='none')
    package_details = db.Column('package_details', db.Text)


class Pool_offers(db.Model):
    """
    Class for creating pool offers

    :args:
        :offer_category: the category of the pool offer
        :offer_pricing: the price of the offer
        :pool_id: the id of the pool to which the offer belongs
    """
    pool_offer_id = db.Column('pool_offer_id', db.Integer, primary_key=True)
    pool_id = db.Column(db.Integer, db.ForeignKey('pool.pool_id', ondelete='CASCADE'),
                        nullable=False)
    offer_category = db.Column('offer_category', db.Text, nullable=False)
    offer_pricing = db.Column('offer_pricing', db.Text, nullable=False)
