from flask import Flask, render_template, redirect, url_for
import time
from user.models import User

@app.route('/dashboard', methods=["POST"])
def dashborad():
    user = User()
    status_code = user.sign_up()
    if status_code != 200:
        time.sleep(2000)
        redirect('/home.html')
    name = user.get_user_name
    return render_template("dashboard.html", user_name = name)