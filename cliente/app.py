import requests
import logging
from flask import Flask, jsonify, request
from flask_caching import Cache
import psycopg2 as pg
#import redis

app = Flask(__name__)
app.config.from_object('config.Config')
cache = Cache(app)

postgres = pg.connect(
        dbname='tarea3',
        user='postgres',
        password='postgres',
        host='postgres',
        port='5432')
cursor = postgres.cursor()

#redis = redis.Redis(host='redis', port=6379, db=0)
#redis.config_set('maxmemory-policy', 'allkeys-lru')
#redis.flushall()
#redis.config_set('maxmemory', '2mb')


@app.route("/uwu", methods=['GET'])
def get_data():
    search = request.args.get('search')
    #cache = redis.get(search.upper())
    app.logger.info(f"Cache: {cache}")
    if cache == None:
        #cursor.execute(f"SELECT * FROM country WHERE name LIKE '%{search.upper()}%'")
        #redis.flushall()
        #data = cursor.fetchall()
        #redis.set(search.upper(), str(data))
        return jsonify(data), "DB"
    else:
        return cache, "REDIS"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)