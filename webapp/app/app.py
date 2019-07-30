from flask import Flask, jsonify, render_template, request
from flask_pymongo import PyMongo
from bson import json_util
import json
import sys

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://148.247.204.173:27017/project'
mongo = PyMongo(app)

#
# CONTROLLERS
#

def getAllMeasurements():
    result = mongo.db.measurements.find()
    documents = []
    for document in result:
        documents.append({
            'idStation': document['idStation'],
            'mediciones': document['mediciones'],
            'dateTime': document['dateTime'],
        })
    return documents



def getStations():
    result = mongo.db.stations.find()
    documents = []
    for document in result:
        documents.append({
            'idStation': document['idStation'],
            'nameStation': document['nameStation'],
            'longitud': document['longitud'],
            'latitud': document['latitud'],
            'elevacion': document['elevacion'],
            'operacion': document['operacion'],
        })
    return documents



#
# HELPERS
#

def abort_if_file_doesnt_exist(filename):
    abort(404, message="File {} doesn't exist".format(filename))



#
# VIEWS
#

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/stations', methods=['GET'])
def stations():
    if request.method == 'GET':
        stations = getStations()
        return jsonify(stations)
    else:
        abort(404, message="Unknown endpoint!")



@app.route('/measurements', methods=['GET'])
def getMeasurements():
    if request.method == 'GET':
        mesurements = getAllMeasurements()
        return jsonify(mesurements)
    else:
        abort(404, message="Unknown endpoint!")
    


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    