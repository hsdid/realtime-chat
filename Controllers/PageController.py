from flask import render_template,request,redirect,url_for,flash,session
from functools import wraps
from passlib.hash import sha256_crypt
from Models.User import *

from app import db, socketio, send, emit,ROOMS
from Controllers.UserController import *

# Check if user logged in


def register_page():

    #if reg_form.validate_on_submit():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        password_equal = request.form['password_equal']

        user_object = User.User.query.filter_by(username=username).first()
        # #Check username exist
        if user_object:
            error = "Someone else has taken this username!"
            return render_template("register.html", error=error)

        if password != password_equal:
            error = "Password don't match"
            return render_template("register.html", error=error)

        password = sha256_crypt.encrypt(str(password))

        user = User.User(username=username, password=password, color='1')
        db.session.add(user)
        db.session.commit()
        # msg = "Acount created, login here :)"
        flash('Acount created, login here','success')
        return redirect(url_for('login'))

    return render_template("register.html")

def login_page():
   #log_form = LoginForm(request.form)

    if request.method == 'POST':
        #get value from form
        username = request.form['username']
        password_candidate = request.form['password']

        # #Check username exist
        user_object = User.User.query.filter_by(username=username).first()

        #if exist check password
        if user_object:
            if sha256_crypt.verify(password_candidate,user_object.password):


                user_id = user_object.id
                color = user_object.color
                session['logged_in'] = True
                session['username'] = username
                session['user_id'] = user_id


                return redirect(url_for('home',rooms=ROOMS, color=color))
            else:

                error = 'Wrong password'
                return render_template('login.html', error=error, )
        else:

            error = 'Username dont exist'
            return render_template('login.html', error=error)

    return render_template('login.html')

def logout_def():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))


def home_page():
    # users = get_users()
    user_object = User.User.query.filter_by(username=session['username']).first()

    if request.method == 'POST':
        # return request.form.get('color')
        user_object.color = request.form.get('colors')
        db.session.commit()

    return render_template('home.html', rooms=ROOMS, color=user_object.color)




