# from flask import render_template,request,redirect,url_for,flash,session
# from Models.Chat import *
# from app import db
#
# def sending_msg():
#
#     if request.method == 'POST':
#
#         sender_id = session['user_id']
#         receiver_id = session['receiver_id']
#         msg = request.form['msg']
#         chat = Chat(sender_id=sender_id,receiver_id=receiver_id,msg=msg)
#
#         db.session.add(chat)
#         db.session.commit()
#
#
#

