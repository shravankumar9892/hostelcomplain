from flask import Flask
from app.config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_heroku import Heroku
import sys

sys.path.insert(0, "/Documents/repos/gallery/svnitsearch/venv/lib/python3.6/site-packages")

app = Flask(__name__, static_url_path='/static')
app.config.from_object(Config)
heroku = Heroku(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models
