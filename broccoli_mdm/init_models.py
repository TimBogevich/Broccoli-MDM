from broccoli_mdm.models import tables
from broccoli_mdm import db

#tabs = tables.query.all()
d = dict()
for row in tables.query.all():
    s = "{ %s }" % row.sql_alchemy_definition
    d[row.name] = type(row.name, (db.Model,), eval(s))
