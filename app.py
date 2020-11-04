from time import localtime, strftime
from flask import Flask,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from Controllers.PageController import *
from Controllers.UserController import *
from Controllers.ChatController import *
from flask_socketio import SocketIO,send,emit,join_room,leave_room



#Configure
app = Flask(__name__)
app.secret_key = 'secret'

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://wnnsdwqvzythjl:932d56a30627bb09be98c7283871940761abd5395a024c0090bc3a8b77545385@ec2-54-217-213-79.eu-west-1.compute.amazonaws.com:5432/dff4o6tse8coad'
    app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
else:
    app.debug = False
    app.config[
        'SQLALCHEMY_DATABASE_URI'] = 'postgres://wnnsdwqvzythjl:932d56a30627bb09be98c7283871940761abd5395a024c0090bc3a8b77545385@ec2-54-217-213-79.eu-west-1.compute.amazonaws.com:5432/dff4o6tse8coad'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
#Initialize Flask-SocketIO
socketio = SocketIO(app)

ROOMS = ["room 1", "room 2", "room 3", "room 4"]



def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
            #return home_page()
        else:
            flash('Unauthorized, Plase login', 'danger')
            return redirect(url_for('login'))

    return wrap

@app.route('/', methods=['POST','GET'])

def index():
    return index_page()

@app.route('/login', methods=['GET','POST'])
def login():

    return login_page()


@app.route('/register', methods=['GET','POST'])
def register():
    return register_page()

@app.route('/logout')
def logout():
    return logout_def()

@app.route('/home', methods=['GET','POST'])
@is_logged_in
def home():

    return home_page()


#@app.route('/home/<string:receiver_id>', methods=['POST','GET'])
@app.route('/home/rooms', methods=['POST','GET'])
@is_logged_in
def user_chat():

    return ROOMS[1]
    #return home_msg(receiver_id)

# @app.route('/home/send_msg', methods=['POST','GET'])
# def send_msg():
#     sending_msg()



@socketio.on('message')
def message(data):
    print(f"\n\n{data}\n\n")

    #sending mesage to all client that connect
    send({'msg':data['msg'], 'username':data['username'], 'time_stamp':
          strftime('%b-%d %I:%M%p', localtime())}, room=data['room'])


@socketio.on('join')
def join(data):

    join_room(data['room'])
    send({'msg': data['username'] + " has joined the " + data['room'] + " room "}, room=data['room'])

@socketio.on('leave')
def leave(data):

    leave_room(data['room'])
    send({'msg': data['username'] + " has left the " + data['room'] + " room "}, room=data['room'])

if __name__ == "__main__":

    socketio.run(app)