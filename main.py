#  mongodb://localhost:27017 local

import email
from urllib import request
from flask import Flask, render_template, redirect, url_for
from pymongo import MongoClient
import json
from bson import json_util
import logging
from config import logging
import time
from user.routes import client_actions


app = Flask(__name__)
# registering the blueprint
app.register_blueprint(client_actions, url_preffix= "")

# creating local connection. only for testing.
client = MongoClient('mongodb://localhost:27017/')
# setting the collection.
database = client['Sample']


@app.route('/')
def hello():
    return render_template("home.html")


@app.route('/sample')
def get_sample():
    collection = database['TODOs']
    get_one = collection.find_one()
    return json.dumps(get_one, default=json_util.default)
    # json.dumps return error since the data return is bson and it has values of type ObjectId 
    # which is not supported by json by default.



# @app.route("task/<tast_name>/<description>")
# def add_task(task_name, description):
#     task_name = str(task_name)
#     description = str(description)
#     id = collection.insert_one({'name': task_name, 'desc': description}).inserted_id
#     return f"<h2> Inserted with iD {id} </h2>"
