# app.py
#https://github.com/GoogleCloudPlatform/community/blob/master/tutorials/building-flask-api-with-cloud-firestore-and-deploying-to-cloud-run.md

# Required imports
import os
from flask import Flask, request, jsonify
#from firebase_admin import credentials, firestore, initialize_app

# Initialize Flask app
app = Flask(__name__)


@app.route("/test1", methods=["GET"])
def books_table_update():
    
    return "This is the test1 backend."

@app.route('/test2', methods=["GET"])
def stanford_page():
    return "This is the test2 backend."

port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=port)