from broccoli_mdm import db


#class tables(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    schema = db.Column(db.String, unique=True) 
#    name = db.Column(db.String)
#    sql_alchemy_definition = db.Column(db.String)
#    is_active = db.Column(db.Integer)

class tables(db.Model):
    __tablename__ = 'tables'