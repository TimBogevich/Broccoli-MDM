from broccoli_mdm import db


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

    
#class tables(db.Model):
#    __tablename__ = 'tables'