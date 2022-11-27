import requests
import logging
from flask import Flask, jsonify, request

from pymongo import MongoClient

client = MongoClient('mongodb://mongo:27017/', username='root', password='tarea3')
db = client['wiki']
collection = db['pages']   

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'message': 'Hello World!'})

@app.route("/uwu", methods=['GET'])
def uwu():
    search = request.args.get('search')
   #search search in mongo
    result = collection.find_one({'title': search})
    if result is None:
        return jsonify({'message': 'Not found'}), 404
    else:
        return jsonify(result), 200


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0' , port=5000)