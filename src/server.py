import json
import sys
from flask import Flask, Response
from flask import request
from flask import jsonify
from flask_cors import CORS
from pymongo import MongoClient
from pprint import pprint
import uuid


#Creating Flask instance in main module -> set for single module
app = Flask(__name__)

#unique resource identifier
uri = "mongodb://owner:Taaz7eem@eg-mongodb.bucknell.edu/ala021"
client = MongoClient(uri)

#Test Database
db = client.ala021

#Table in Test 'db'
collection = db.test


@app.route('/videos/<v_param>)
def add_video()

@app.route('/star/', methods=['GET'])


#Database Attributes
#{name: string, embed: string, description: string, tags: string}

#@app.route('/video/<params>')


