from broccoli_mdm.models import tables, connections
from broccoli_mdm import db, app

app.config["SQLALCHEMY_BINDS"] = dict()

for con in connections.query.all():
    app.config["SQLALCHEMY_BINDS"][con.schema] = con.connection_string

try:
    db.reflect()
except Exception as e:
    print(e)

table_class_objects = dict()
for row in tables.query.all():
    if row.is_active == 1:
        class_name = row.name.lower()
        class_definition = {"__bind_key__": row.schema, "__tablename__": class_name}
        try:
            table_class_objects[class_name] = type(class_name, (db.Model,), class_definition)
        except Exception as e:
            print(e)
