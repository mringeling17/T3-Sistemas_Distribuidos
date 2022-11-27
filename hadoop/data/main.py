import wikipedia as wiki
from pymongo import MongoClient
import os
import time
import json

client = MongoClient('mongodb://mongo:27017/', username='root', password='tarea3')
db = client['wiki']

collection = db['pages']    
collection.delete_many({})
collection.create_index([('word', 1)], unique=True)

print('-'*200)
artists = ["Bad Bunny", "Dua Lipa", "Ariana Grande", "Karol_G", "The Weeknd", "Justin Bieber", "Post Malone", "Ed Sheeran", "Taylor Swift", "Bizarrap"]
wiki.set_lang('es')
count = 1
folder = "./carpeta1/"
if not os.path.exists(folder):
    os.makedirs(folder)
    os.makedirs("./carpeta2/")
for i in artists:
    a = wiki.page(i)
    if count>5:
        folder = "./carpeta2/"
    with open(folder+str(count) + '.txt', 'w', encoding='utf-8') as f:
        f.write(a.content)
    count += 1
if not os.path.exists("./output/"):
    os.makedirs("./output/")
if os.path.exists("./output/output.json"):
    os.remove("./output/output.json")
print('-'*200)

while True:
    time.sleep(2)
    print("Waiting for Hadoop output file...")
    if os.path.exists("./output/output.json"):
        print("FILE FOUND!")
        #insert key value pairs into mongo
        with open("./output/output.json", 'r', encoding='utf-8') as f:
            data = json.load(f)
            for i in data:
                collection.update_one({'word': i}, {'$set': {'word': i, 'count': data[i]}}, upsert=True)
                        
        print("HADOOP DATA INSERTED INTO MONGODB")
        break
print('-'*200)

