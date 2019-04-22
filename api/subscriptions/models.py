from api.database.db import db


class Subscribe(db.Model):
    __tablename__ = 'subscriptions'
    subscription_id = db.Column('subscription_id',
                                db.Integer, primary_key=True)
    user_id = db.Column('user_id', db.Integer,
                        db.ForeignKey('user.user_id'), nullable=False)
    pool_id = db.Column('pool_id', db.Integer,
                        db.ForeignKey('pool.pool_id'), nullable=False)
    sub_name = db.Column('sub_name', db.String(150), nullable=False)
    sub_typ = db.Column('sub_type', db.String(30), nullable=True)

    def __repr__(self):
        return 'Subscription {}'.format(self.subscription_id)
