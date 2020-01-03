#!/usr/bin/python

import json

from flask import request
from app import app

@app.route('/')
def hello():
    return "\n\nWelcome to the wolrd of magics!\n\n"

@app.route('/getavg', methods=['POST'])
def CalculateAvarage():
    marks = request.data
    marks = json.loads(marks)
    avg = sum(marks)/len(marks)
    avarage = {"avg": avg}

    return json.dumps(avarage)
    # return "\n\nAvarage is : {}\n\n".format(avg)


@app.route('/about', methods=['GET'])
def about():
    msg = '''\n
        This is sample flask server testing.
        Will be implemented later on.
        \n'''
    return msg
