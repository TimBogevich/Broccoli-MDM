from broccoli_mdm import db,login_manager
from flask_login import UserMixin
import hashlib
import json

class ClassToolkit():
    @classmethod
    def getAttributes(cls):
        var = vars(cls)
        var = filter(lambda x: "__" not in x, var)
        var = filter(lambda x: "getAttributes" not in x, var)
        var = filter(lambda x: "_sa_class_manager" not in x, var)
        return json.dumps(list(var))

class tables(db.Model,ClassToolkit):
    id = db.Column(db.Integer, primary_key=True)
    schema = db.Column(db.String) 
    name = db.Column(db.String, unique=True)
    sql_alchemy_definition = db.Column(db.String)
    is_active = db.Column(db.Integer)

class connections(db.Model,ClassToolkit):
    id = db.Column(db.Integer, primary_key=True)
    schema = db.Column(db.String, unique=True) 
    connection_string = db.Column(db.String)

class users(db.Model,UserMixin,ClassToolkit):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String, unique=True)
    email = db.Column(db.String)
    password_md5 = db.Column(db.String)
    salt = db.Column(db.String)
    def get_id(self):
        return (self.id)
    def check_password(user_name, password):
        user = users.query.filter_by(user_name=user_name).first()
        hash = hashlib.md5(password.encode("utf-8")).hexdigest().upper()
        if (hash + user.salt) == (user.password_md5 + user.salt):
            return user
            
class permissions(db.Model,UserMixin,ClassToolkit):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    table_id = db.Column(db.Integer)
    read_flag = db.Column(db.SmallInteger)
    edit_flag = db.Column(db.SmallInteger)
    delete_flag = db.Column(db.SmallInteger)
    __table_args__ = (db.UniqueConstraint("user_id", "table_id"),)