from broccoli_mdm.models import tables, connections
from broccoli_mdm import db, app

app.config["SQLALCHEMY_BINDS"] = dict()

for con in connections.query.all():
    app.config["SQLALCHEMY_BINDS"][con.schema] = con.connection_string


db.reflect()

d = dict()
for row in tables.query.all():
    if row.is_active == 1:
        s = """class %s(db.Model):
                __bind_key__ = '%s'
                __tablename__ = '%s'""" % (row.name.lower(), row.schema, row.name.lower())
        exec(s)
        d[row.name] = eval(row.name.lower())



