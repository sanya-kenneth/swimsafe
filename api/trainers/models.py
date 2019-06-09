from api.database.db import db


class Trainer(db.Model):
    trainer_id = db.Column('trainer_id', db.Integer, primary_key=True)
    first_name = db.Column('first_name', db.String(80), nullable=False)
    last_name = db.Column('last_name', db.String(80), nullable=False)
    working_time = db.Column('working_time', db.Text, nullable=False)
    description = db.Column('description', db.Text, nullable=False)
    available = db.Column('available', db.String(80), nullable=True,
                          default="available")
    pool_id = db.Column(db.Integer, db.ForeignKey('pool.pool_id', ondelete='CASCADE'),
                        nullable=False)
    trainer_img = db.Column('trainer_img', db.Text, nullable=True)

    def __repr__(self):
        return 'Trainer %r' % self.first_name + " " + self.last_name
