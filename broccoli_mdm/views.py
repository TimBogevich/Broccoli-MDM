from flask import render_template, request, redirect, url_for
from broccoli_mdm import app, login_manager
from flask_login import current_user, login_required, login_user, logout_user
from broccoli_mdm.models import users
import hashlib 


@login_manager.user_loader
def load_user(id):
    return users.query.filter_by(id=id).first()


@app.route('/')
@login_required
def index():
    return render_template(
        'index.html',
        title='Home Page',
    )

@app.route('/table/<tablename>')
@login_required
def tables(tablename):
    return render_template(
        'table.html',
        title='Table editor',
    )


@app.route('/admin/<path>')
@login_required
def admin(path):
    return render_template(
        'admin_tables.html',
        title='Preferences editor')


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        if current_user.is_authenticated:
            print(current_user.email)
            return redirect(url_for("index"))
        else:
            return render_template("login.html")
    elif request.method == "POST":
        input = request.get_json()
        try:
            user = users.check_password(input["user_name"], input["password"])
            login_user(user)
            return "success"
        except Exception as e:
            print(e)
            return "Fail: username or password incorrect. Please contact to your system administrator"


@app.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))