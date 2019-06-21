import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_BINDS = {'Test' : 'sqlite:///C:\\GIT\\Broccoli-MDM\\broccoli_mdm\\data.db'}
    SQLALCHEMY_TRACK_MODIFICATIONS = True
