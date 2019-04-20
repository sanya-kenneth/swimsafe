from api.database.db import db


class Images(db.Model):
    image_id = db.Column('image_id', db.Integer, primary_key=True)
    image_name = db.Column('image_name', db.Text)
    image_url = db.Column('image_url', db.Text)
    pool_id = db.Column(db.Integer, db.ForeignKey('pool.pool_id'),
                        nullable=False)


    def __repr__(self):
        return self.image_name
