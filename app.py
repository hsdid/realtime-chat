from flask import Flask
from Controllers.UserController import user
from Controllers.PageController import index_page
from wtfform import *

#Configure
app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/', methods=['GET','POST'])
def index():
    return index_page()

if __name__ == "__main__":

    app.run(debug=True)