from Models import User
from flask_sqlalchemy import *
#return all users

def get_users():
    # users = User.User.query.all()
    #users = User.db.session.query(User.User).all()
    users = User.db.session.execute('SELECT * FROM users')

    return users
def get_user(id):

    #user = User.db.session.execute("SELECT * FROM users WHERE id = %s",(id))
    user = User.User.query.filter_by(id=id).first()


    return user.username

