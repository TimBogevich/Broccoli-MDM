from broccoli_mdm import db


#class Countries(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    country_name = db.Column(db.String(64), index=True, unique=True)
#    iso_code = db.Column(db.String(120), index=True, unique=True)
#    currency_code = db.Column(db.String(128))

Column = db.Column

class tables(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    schema = db.Column(db.String, unique=True) 
    name = db.Column(db.String)
    sql_alchemy_definition = db.Column(db.String)
    is_active = db.Column(db.Integer)


attr_dict = {
        'id': Column(db.Integer, primary_key=True),
	    'country_name': Column(db.String(64), index=True, unique=True),
        'iso_code' : Column(db.String(120), index=True, unique=True),
        'currency_code' : Column(db.String(128))}


Countries = type('Countries', (db.Model,), attr_dict)