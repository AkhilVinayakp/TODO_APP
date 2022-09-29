
'''
Creating using blueprints

'''
from flask import Blueprint, render_template, redirect, session
from user.models import User

client_actions = Blueprint('client_actions', '__name__', static_folder='../static', template_folder='../templates')

@client_actions.route('/dashboard', methods=['POST', 'GET'])
def dashborad():
    user = User()
    status_code = user.sign_up()
    if status_code != 200:
        redirect('/home.html')
    name = user.get_user_name
    return render_template("dashboard.html", user_name = name)

