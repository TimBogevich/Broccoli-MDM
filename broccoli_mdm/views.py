from flask import render_template
from broccoli_mdm import app

@app.route('/')
def home():
    return render_template(
        'index.html',
        title='Home Page',
    )


@app.route('/table/<tablename>')
def tables(tablename):
    return render_template(
        'table.html',
        title='Table editor',
    )


@app.route('/admin/<path>')
def admin(path):
    return render_template(
        'admin_tables.html',
        title='Preferences editor',
    )
