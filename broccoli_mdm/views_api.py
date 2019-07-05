from flask import render_template
from broccoli_mdm import app, manager
from broccoli_mdm.init_models import *
from sqlalchemy.inspection import inspect
from broccoli_mdm.models import tables, connections, users, permissions
from flask_login import current_user, login_required, login_user, logout_user

#Generate API for list of taybles
for obj in d:
    manager.create_api(d[obj], methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])

manager.create_api(tables, methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])

manager.create_api(connections, methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])

manager.create_api(users, methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'], exclude_columns=["password_md5", "salt"])

manager.create_api(permissions, methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])


@app.route('/api_service/pk/<class_name>')
def api_tech_pk(class_name):
    return inspect(eval(class_name)).primary_key[0].name

@app.route('/api_service/attributes/<class_name>')
def api_tech_attributes(class_name):
    return eval(class_name).getAttributes()