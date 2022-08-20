from flask import Flask, request, make_response, jsonify
#import pandas as pd
#import gcsfs
#import pandas_gbq
#import os

app = Flask(__name__)
#app.config["DEBUG"] = True #If the code is malformed, there will be an error shown when visit app

@app.route("/test1", methods=["GET"])
def books_table_update():
    
    return "This is the test1 backend"

@app.route('/test2', methods=["GET"])
def stanford_page():
    return "This is the test2 backend"
    