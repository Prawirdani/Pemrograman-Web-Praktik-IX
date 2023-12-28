from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)


## Inisiasi ORM SQLAlchemy
db = SQLAlchemy(app)
## Inisiasi migrations tools
migrate = Migrate(app, db)

from app import routes
from app.model import user, todo
