from app import db

class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    color = db.Column(db.String())
    # def __init__(self, username, password):
    #     self.username = username
    #     self.password = password

