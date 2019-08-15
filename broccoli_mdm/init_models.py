from broccoli_mdm.models import tables, connections
from broccoli_mdm import db, app

app.config["SQLALCHEMY_BINDS"] = dict()

for con in connections.query.all():
    app.config["SQLALCHEMY_BINDS"][con.schema] = con.connection_string

try:
    db.reflect()
except Exception as e:
    print(e)    

d = dict()
for row in tables.query.all():
    if row.is_active == 1:
        s = f"""class {row.name.lower()} (db.Model):
                __bind_key__ = '{row.schema}'
                __tablename__ = '{row.name.lower()}'""" 
        try:
            exec(s)
            d[row.name] = eval(row.name.lower())
        except Exception as e: 
            print(e)



