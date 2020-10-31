from flask_wtf import FlaskForm
from wtforms import  StringField, PasswordField,validators
from wtforms.validators import ValidationError


#Register Form class
class RegisterForm(FlaskForm):


    username = StringField('Username', [validators.Length(min=4, max=25)])
    # email = StringField('Email', [validators.Length(min=6, max=50)])

    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message="Password do not match")
    ])
    confirm = PasswordField('Confirm Password')

    # def validate_username(self, username):
    #     user_object = User.query.filter_by(username=username.data).first()
    #     if user_object:
    #         raise ValidationError("User name already exist plase use another username")

class LoginForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    password = PasswordField('Password', [validators.DataRequired()])