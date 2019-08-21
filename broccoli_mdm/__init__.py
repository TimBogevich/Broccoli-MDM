from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from broccoli_mdm.config import Config
from flask_restless import APIManager
from flask_migrate import Migrate
import os
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn=os.environ.get("SENTRY_KEY"),
    integrations=[FlaskIntegration()]
)

app = Flask(__name__)
app.secret_key = os.environ.get("BROCCOLI_SECRET_KEY")
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = APIManager(app, flask_sqlalchemy_db=db)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


import broccoli_mdm.models # NOQA
import broccoli_mdm.init_models # NOQA
import broccoli_mdm.views # NOQA
import broccoli_mdm.views_api # NOQA