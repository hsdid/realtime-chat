from app import db

class Chat(db.Model):

    __tablename__ = "chats"

    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, nullable=False)
    receiver_id = db.Column(db.Integer, nullable=False)
    msg = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.TIMESTAMP)

    # def __init__(self, username, password):
    #     self.username = username
    #     self.password = password