#  mongodb://localhost:27017 local

from flask import Flask
app = Flask(__name__)
import pymongo
from pymongo import MongoClient
import json
from bson import json_util

# creating local connection
client = MongoClient('mongodb://localhost:27017/')
# setting the collection.
database = client['Sample']
collection = database['TODOs']

@app.route('/')
def hello():
    return "working may"


@app.route('/sample')
def get_sample():
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
