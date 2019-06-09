from broccoli_mdm import db


class Countries(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country_name = db.Column(db.String(64), index=True, unique=True)
    iso_code = db.Column(db.String(120), index=True, unique=True)
    currency_code = db.Column(db.String(128))


