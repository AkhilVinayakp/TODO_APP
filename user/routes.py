
'''
Creating using blueprints

'''
from ast import arg
from flask import Blueprint, render_template, redirect, session
from user.models import User
from functools import wraps

client_actions = Blueprint('client_actions', '__name__', static_folder='../static', template_folder='../templates')

# decorator to check the login status
def is_login(func):
    @wraps(func)
    def check_in_session(*args, **kargs):
        if 'logged_in' in session:
            return func(*args, **kargs)
        else:
            redirect('/')
    return check_in_session


@is_login
@client_actions.route('/dashboard', methods=['POST', 'GET'])
def dashborad():
    user = User()
    status_code = user.sign_up()
    if status_code != 200:
        redirect('/home.html')
    name = user.get_user_name
    return render_template("dashboard.html", user_name = name)

@client_actions.route('/signout', methods=['GET'])
def signout(self):
    session.clear()
    redirect('/')