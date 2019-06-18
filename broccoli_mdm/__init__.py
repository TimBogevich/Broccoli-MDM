from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from broccoli_mdm.config import Config
from flask_restless import APIManager
from flask_migrate import Migrate



app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = APIManager(app, flask_sqlalchemy_db=db)


import broccoli_mdm.models
import broccoli_mdm.init_models
import broccoli_mdm.views
import broccoli_mdm.views_api