from flask import render_template
from broccoli_mdm import app, manager
from broccoli_mdm.models import Countries


#API endpoint: countries
manager.create_api(Countries, methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])