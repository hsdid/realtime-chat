from flask import render_template
from wtfform import *
def index_page():


    reg_form = RegisterForm()
    reg_form.validate_on_submit()
    return render_template("index.html", form = reg_form)