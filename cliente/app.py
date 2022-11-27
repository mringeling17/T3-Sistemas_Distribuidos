import logging
import requests
import wikipedia as wiki
from pymongo import MongoClient
#flask logs
logging.basicConfig(level=logging.DEBUG)
from flask import Flask, jsonify, request

client = MongoClient('mongodb://mongo:27017/', username='root', password='tarea3')
db = client['wiki']
collection = db['pages']   
links = ["Bad Bunny", "Dua Lipa", "Ariana Grande", "Karol_G", "The Weeknd", "Justin Bieber", "Post Malone", "Ed Sheeran", "Taylor Swift", "Bizarrap"]
urls = ["https://es.wikipedia.org/wiki/Bad_Bunny", "https://es.wikipedia.org/wiki/Dua_Lipa", "https://es.wikipedia.org/wiki/Ariana_Grande", "https://es.wikipedia.org/wiki/Karol_G", "https://es.wikipedia.org/wiki/The_Weeknd", "https://es.wikipedia.org/wiki/Justin_Bieber", "https://es.wikipedia.org/wiki/Post_Malone", "https://es.wikipedia.org/wiki/Ed_Sheeran", "https://es.wikipedia.org/wiki/Taylor_Swift", "https://es.wikipedia.org/wiki/Bizarrap"]

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'message': 'Hello World!'})
@app.route("/uwu", methods=['GET'])
def uwu():
    search = request.args.get('search')
    search = search.lower()
    app.logger.info("search: " + search)
    documents = []
    document_reps = []
    ret = []
    if search is None:
        return jsonify({'message': 'No search query'})
    else:
        result = collection.find_one({'word': search})
        app.logger.info(result)
        if result is None:
            return jsonify({'message': 'No results'})
        else:
            count = result['count']
            app.logger.info(count)
            for i in count:
                document = i
                reps = count[document]
                documents.append(document)
                document_reps.append(reps)
            for i in range(len(document_reps)):
                for j in range(0, len(document_reps)-i-1):
                    if document_reps[j] < document_reps[j+1] :
                        document_reps[j], document_reps[j+1] = document_reps[j+1], document_reps[j]
                        documents[j], documents[j+1] = documents[j+1], documents[j]
            for i in range(len(documents)):
                url_pos = int(documents[i])-1
                url = urls[url_pos]
                reps = document_reps[i]
                a = {'url': url, 'reps': reps}
                ret.append(a)
            return jsonify({'message': 'Resultados de la busqueda ordenados por repeticiones de la palabra', 'result': ret})
@app.route("/uwu2", methods=['GET'])
def uwu2():
    search = request.args.get('search')
    search = search.lower()
    app.logger.info("search: " + search)
    mayor = 0
    doc_mayor = 0
    if search is None:
        return jsonify({'message': 'No search query'})
    else:
        result = collection.find_one({'word': search})
        app.logger.info(result)
        if result is None:
            return jsonify({'message': 'No results'})
        else:
            count = result['count']
            #word: "000"
            #count:  [{"1": 2}, {"2": 1}, {"3": 5}, {"5": 10}, {"6": 8}, {"7": 4}, {"8": 9}, {"9": 14}],
            app.logger.info(count)
            for i in count:
                reps = count[i]
                if reps > mayor:
                    mayor = reps
                    doc_mayor = i
            url_pos = int(doc_mayor)-1
            url = urls[url_pos]
            return jsonify({'message': 'URL con mayor repeticiones de la palabra', 'result': url, 'reps': mayor})
  
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0' , port=5000)