from flask import render_template
from broccoli_mdm import app, manager
from broccoli_mdm.init_models import *
from sqlalchemy.inspection import inspect

for obj in d:
    manager.create_api(d[obj], methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])


@app.route('/api_service/pk/<class_name>')
def api_tach_models(class_name):
    return inspect(eval(class_name)).primary_key[0].name