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
    dsn="https://b2424598065b4ef7a5ce1e5ad3d613b6@sentry.io/1533462",
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


import broccoli_mdm.models
import broccoli_mdm.init_models
import broccoli_mdm.views
import broccoli_mdm.views_api