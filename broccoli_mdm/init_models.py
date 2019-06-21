from broccoli_mdm.models import tables, connections
from broccoli_mdm import db, Config, app



db.reflect()

d = dict()
for row in tables.query.all():
    if row.is_active == 1:
        s = """class %s(db.Model):
                __bind_key__ = 'Test'
                __tablename__ = '%s'""" % (row.name.lower(), row.name.lower())
        exec(s)
        d[row.name] = eval(row.name.lower())



