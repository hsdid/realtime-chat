from flask import render_template,request,redirect,url_for,flash,session
from functools import wraps
from wtfform import *
from passlib.hash import sha256_crypt
from Models.User import *
from app import db


# Check if user logged in


def register_page():
    reg_form = RegisterForm(request.form)
    log_form = LoginForm(request.form)
    #if reg_form.validate_on_submit():
    if request.method == 'POST' and reg_form.validate():
        username = reg_form.username.data
        password = sha256_crypt.encrypt(str(reg_form.password.data))

        # #Check username exist
        user_object = User.query.filter_by(username=username).first()
        if user_object:
            error = "Someone else has taken this username!"
            return render_template("register.html", form=reg_form, error=error)

        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        msg = "Acount created, login here :)"
        return render_template('login.html', msg=msg,form = log_form)

    return render_template("register.html", form=reg_form)

def login_page():
    log_form = LoginForm(request.form)

    if request.method == 'POST':
        #get form fields
        username = log_form.username.data
        password_candidate = log_form.password.data
        # #Check username exist
        user_object = User.query.filter_by(username=username).first()
        #if exist check password
        if user_object:
            if sha256_crypt.verify(password_candidate,user_object.password):

                msg = 'logged successfully'
                user_id = user_object.id

                session['logged_in'] = True
                session['username'] = username
                session['id'] = user_id

                return redirect(url_for('home', msg=msg))

            else:

                error = 'Wrong password'
                return render_template('login.html', error=error, form=log_form)
        else:

            error = 'Username dont exist'
            return render_template('login.html', error=error, form=log_form)

    return render_template('login.html', form=log_form)

def logout_def():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))

def index_page():

    return render_template('index.html')

def home_page():

    return render_template('home.html')