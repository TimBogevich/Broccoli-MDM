from flask import request, Response
from broccoli_mdm import app, manager
from broccoli_mdm.init_models import table_class_objects
from sqlalchemy.inspection import inspect
from broccoli_mdm.models import tables, connections, users, permissions
from flask_login import current_user, login_required
import flask_restless
from sqlalchemy import func
from alchemyjsonschema import SchemaFactory
from alchemyjsonschema import Classifier
from alchemyjsonschema import NoForeignKeyWalker
from json import dumps
import sqlalchemy.types as t
import sys

exclude_columns = ["password_md5", "salt"]


def check_permissions(**kw):
    if current_user.sysadmin == 1:
        return
    # extracting tablename from URL
    table_name = request.path.split("/")[-1:][0]
    curr_user = current_user.id if hasattr(current_user, "id") else None
    table = tables.query.filter(func.lower(tables.name) == table_name).first()
    permission = permissions.query.filter_by(
        table_id=table.id, user_id=curr_user).first()
    if permission is None:
        raise flask_restless.ProcessingException(code=401)
    if request.method == "GET" and permission.read_flag == 1:
        return
    elif request.method == "PUT" and permission.edit_flag == 1:
        return
    elif request.method == "POST" and permission.edit_flag == 1:
        return
    elif request.method == "DELETE" and permission.delete_flag == 1:
        return
    else:
        raise flask_restless.ProcessingException(code=401)


preprocessors = dict(GET_MANY=[check_permissions],
                     GET_SINGLE=[check_permissions],
                     POST=[check_permissions],
                     PUT_SINGLE=[check_permissions],
                     PUT_MANY=[check_permissions],
                     DELETE_MANY=[check_permissions],
                     DELETE_SINGLE=[check_permissions])

tables_prepr = dict(POST=[check_permissions],
                    PUT_SINGLE=[check_permissions],
                    PUT_MANY=[check_permissions],
                    DELETE_MANY=[check_permissions],
                    DELETE_SINGLE=[check_permissions])

methods=['GET', 'POST', 'PATCH', 'DELETE']


# Generate API for list of taybles
for obj in table_class_objects: # NOQA
    manager.create_api(table_class_objects[obj], # NOQA
                       methods=methods,
                       preprocessors=preprocessors,
                       results_per_page=0)


manager.create_api(tables, methods=methods, preprocessors=tables_prepr)

manager.create_api(connections, methods=methods, preprocessors=preprocessors)

manager.create_api(users, methods=methods, exclude_columns=exclude_columns, preprocessors=preprocessors)

manager.create_api(permissions, methods=methods, preprocessors=preprocessors)


@login_required
@app.route('/api_service/create_new_user', methods=["POST"])
def api_tech_create_new_user():
    input = request.get_json()
    if input["user_name"] != "" and input["email"] != "" and input["user_name"] != "":
        users.create_new_user(
            user_name=input["user_name"], email=input["email"], password=input["password"])
        return "success"


@app.route('/api_service/check_connection', methods=["POST"])
def api_tech_check_connection(connection_text=None):
    input = request.get_json()
    connection_text = input.get("connection_text") or connection_text
    try:
        from sqlalchemy import create_engine
        engine = create_engine(connection_text)
        con = engine.connect()
        con.execute("select 1")
        return Response("Connection success", status=200)
    except Exception as e:
        print(e)
        return Response("Can't connect to database: " + str(e), status=400)


@app.route('/api_service/get_schema/<class_name>')
def api_tech_get_schema(class_name):
    column_to_schema = {
        t.String: "text",
        t.Text: "text",
        t.Integer: "numeric",
        t.SmallInteger: "checkbox",
        t.BigInteger: "text",
        t.Numeric: "numeric",
        t.Float: "numeric",
        t.DateTime: "date",
        t.Date: "date",
        t.Enum: "text",
    }

    if class_name in ["tables", "connections", "users", "permissions"]:
        class_object = getattr(sys.modules[__name__], class_name)
    else:
        class_object = table_class_objects[class_name]

    classifier = Classifier(mapping=column_to_schema)
    factory = SchemaFactory(classifier=classifier, walker=NoForeignKeyWalker)
    schema = factory(class_object, excludes=exclude_columns)
    dic = list()
    headers = list()
    for i in schema["properties"].items():
        column = {
            "data": i[0],
            "type": i[1]["type"],
            "required": i[0] in schema["required"]
        }
        if i[1]["type"] == "checkbox":
            column["checkedTemplate"] = 1
            column["uncheckedTemplate"] = 0
        dic.append(column)
        headers.append(i[0])
    schema["properties"] = dic
    schema["headers"] = headers
    schema["primaryKey"] = inspect(class_object).primary_key[0].name
    return dumps(schema)



@app.route('/shutdown', methods=['POST'])
def shutdown():
    def shutdown_server():
        func = request.environ.get('werkzeug.server.shutdown')
        if func is None:
            raise RuntimeError('Not running with the Werkzeug Server')
        func()
        
    shutdown_server()
    return 'Server shutting down...'