from api.database.db import db


class RateTrainer(db.Model):
    rate_id = db.Column('rate_id', db.Integer, primary_key=True)
    trainer_rating = db.Column('trainer_rating', db.Integer, nullable=False)
    user_id = db.Column('user_id', db.Integer,
                        db.ForeignKey('user.user_id',
                                      ondelete='CASCADE'), nullable=False)
    trainer_id = db.Column('trainer_id', db.Integer,
                           db.ForeignKey('trainer.trainer_id',
                                         ondelete='CASCADE'), nullable=False)
