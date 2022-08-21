# app.py
#https://github.com/GoogleCloudPlatform/community/blob/master/tutorials/building-flask-api-with-cloud-firestore-and-deploying-to-cloud-run.md

# Required imports
import os
from flask import Flask, request, jsonify
from google.cloud import firestore
#from firebase_admin import credentials, firestore, initialize_app

# Initialize Flask app
app = Flask(__name__)


@app.route("/test1", methods=["GET"])
def test1():
    
    return "This is the test1 backend."

@app.route('/test2', methods=["GET"])
def test2():
    return "This is the test2 backend."

@app.route('/dataset-test', methods=["GET"])
def dataset-test():
    #fs = firestore.Client()
    #league = 'nba'
    #bq_table = 'api_game_team_odds_ml'
    #docs = fs.collection(u'sports_analytics').document(league).collection(bq_table).stream()
    ##docs = fs.collection('users').where('paid', '==', True).stream()
    #data = []
    #for doc in docs:
    #    #print(doc.id)
    #    #print(doc.to_dict())
    #    data.append(doc.to_dict())
    ##headers = {
    ##        'Access-Control-Allow-Origin': '*'
    ##    }
    ##return ({"data":data}, 200, headers)
    #return({"data":data})
    return "test dataset-test"

port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=port)