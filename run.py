from api import create_app
from flask_migrate import Migrate
from api.database.db import db


app = create_app('Development')
# Setup migration engine
migrate = Migrate(app, db)
# Entry point into the api
if __name__ == '__main__':
    app.run()
