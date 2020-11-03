from flask import Flask,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from Controllers.PageController import *
from Controllers.UserController import *
from Controllers.ChatController import *
from flask_socketio import SocketIO,send,emit



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
socketio = SocketIO(app)

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


@app.route('/home/<string:receiver_id>', methods=['POST','GET'])
@is_logged_in
def user_chat(receiver_id):
    return home_msg(receiver_id)

# @app.route('/home/send_msg', methods=['POST','GET'])
# def send_msg():
#     sending_msg()

@socketio.on('message')
def message(data):
    # print(f"\n\n{data}\n\n")
    send(data)


if __name__ == "__main__":

    socketio.run(app)