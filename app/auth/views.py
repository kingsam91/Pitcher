from flask import render_template
from . import auth
from flask_login import login_required

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('auth/login.html')