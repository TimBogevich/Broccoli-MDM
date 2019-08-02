from broccoli_mdm import db,login_manager
from flask_login import UserMixin
import hashlib
import json



class tables(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    schema = db.Column(db.String) 
    name = db.Column(db.String, unique=True)
    sql_alchemy_definition = db.Column(db.String)
    is_active = db.Column(db.SmallInteger)

class connections(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    schema = db.Column(db.String, unique=True) 
    connection_string = db.Column(db.String)

class users(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, nullable=False)
    sysadmin = db.Column(db.SmallInteger)
    password_md5 = db.Column(db.String, nullable=False)
    salt = db.Column(db.String)
    def get_id(self):
        return (self.id)
    def check_password(user_name, password):
        user = users.query.filter_by(user_name=user_name).first()
        hash = hashlib.md5(password.encode("utf-8")).hexdigest().upper()
        if (hash) == (user.password_md5):
            return user
    def create_new_user(user_name, email, password):
        hash = hashlib.md5(password.encode("utf-8")).hexdigest().upper()
        user = users(user_name=user_name, email=email, password_md5=hash)
        db.session.add(user)
        db.session.commit()


            
class permissions(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    table_id = db.Column(db.Integer)
    read_flag = db.Column(db.SmallInteger)
    edit_flag = db.Column(db.SmallInteger)
    delete_flag = db.Column(db.SmallInteger)
    __table_args__ = (db.UniqueConstraint("user_id", "table_id"),)



