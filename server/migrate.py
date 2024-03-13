from flask_migrate import Migrate

from main import *

migrate = Migrate(app, db)