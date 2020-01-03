#!/usr/bin/python

import ast
import json
import requests

url = "http://127.0.0.1:5000/"


def printErrorMsg(resp):
    msg = ("\nRequest failed with status code: {} "
        "and err message: {}".format(resp.status_code,
                                        resp.text))
    print msg

# posting the data and getting back the computed response
marks=[86, 84, 80, 73, 88, 89]
resp = requests.post(url=url+"getavg", data=json.dumps(marks), timeout=60)
if resp.status_code == 200:
    print "\nRequest succeeded"
    output = ast.literal_eval(resp.text)
    print output
else:
    printErrorMsg(resp)


# get the simple message from the app server
resp = requests.get(url=url, timeout=60)
if resp.status_code == 200:
    print resp.text
else:
    printErrorMsg(resp)
