from bringmfapp import app
from bringmfapp import login_manager

from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

from mockdbhelper import MockDBHelper as DBHelper
from user import User
from passwordhelper import PasswordHelper

from flask.ext.login import login_required
from flask.ext.login import login_user
from flask.ext.login import logout_user


DB = DBHelper()
app.secret_key = 'WcYEKV0r1QTOAEa+a0AAJKwMc3c5v+pPgNu1CbgwpV7p3cZklgtpf17lqdkVnB9UeEcmD4NhVRctwPFYfnfan4K8wnxlNWPLPgeY'
PH = PasswordHelper()


@login_manager.user_loader
def load_user(user_id):
    user_password = DB.get_user(user_id)
    if user_password:
        return User(user_id)


@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    stored_user = DB.get_user(email)
    if stored_user and PH.validate_password(password, stored_user['salt'], stored_user['hashed']):
        user = User(email)
        login_user(user, remember=True)
        return redirect(url_for('account'))
    return home()


@app.route("/register", methods=["POST"])
def register():
    email = request.form.get("email")
    pw1 = request.form.get("password")
    pw2 = request.form.get("password2")
    if not pw1 == pw2:
        return redirect(url_for('home'))
    if DB.get_user(email):
        return redirect(url_for('home'))
    salt = PH.get_salt()
    hashed = PH.get_hash(pw1 + salt)
    DB.add_user(email, salt, hashed)
    return redirect(url_for('home'))


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/account")
@login_required
def account():
    return "You are logged in"


