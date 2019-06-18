from broccoli_mdm.models import tables
from broccoli_mdm import db


db.reflect()

tabs = tables.query.all()
d = dict()
for row in tables.query.all():
    s = "class %s(db.Model): __tablename__ = '%s'" % (row.name.lower(), row.name.lower())
    exec(s)
    d[row.name] = eval(row.name.lower())



