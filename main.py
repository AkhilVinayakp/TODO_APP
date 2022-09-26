#  mongodb://localhost:27017 local

from urllib import request
from flask import Flask, render_template, request
app = Flask(__name__)
from pymongo import MongoClient
import json
from bson import json_util
# importing user routes
from user import routes



# creating local connection
client = MongoClient('mongodb://localhost:27017/')
# setting the collection.
database = client['Sample']
collection = database['TODOs']

@app.route('/')
def hello():
    return render_template("home.html")


@app.route('/sample')
def get_sample():
    get_one = collection.find_one()
    return json.dumps(get_one, default=json_util.default)
    # json.dumps return error since the data return is bson and it has values of type ObjectId 
    # which is not supported by json by default.


@app.route('/dashboard', methods=["POST"])
def dashborad():
    # getting the variables
    name = request.form.get('name')
    
    return render_template("dashboard.html")






# @app.route("task/<tast_name>/<description>")
# def add_task(task_name, description):
#     task_name = str(task_name)
#     description = str(description)
#     id = collection.insert_one({'name': task_name, 'desc': description}).inserted_id
#     return f"<h2> Inserted with iD {id} </h2>"
