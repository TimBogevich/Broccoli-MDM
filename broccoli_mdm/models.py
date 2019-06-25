from broccoli_mdm import db,login_manager
from flask_login import UserMixin
import hashlib

class tables(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    schema = db.Column(db.String) 
    name = db.Column(db.String, unique=True)
    sql_alchemy_definition = db.Column(db.String)
    is_active = db.Column(db.Integer)

class connections(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    schema = db.Column(db.String, unique=True) 
    connection_string = db.Column(db.String)

class Users(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String, unique=True)
    email = db.Column(db.String)
    password_md5 = db.Column(db.String)
    salt = db.Column(db.String)
    def get_id(self):
        return (self.id)
    def check_password(user_name, password):
        user = Users.query.filter_by(user_name=user_name).first()
        hash = hashlib.md5(password.encode("utf-8")).hexdigest().upper()
        if (hash + user.salt) == (user.password_md5 + user.salt):
            return user
            

#