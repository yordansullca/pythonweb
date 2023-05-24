from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)
client = MongoClient("mongodb+srv://dbtesis:bIatfhaxzZdPmyGk@cluster0.iklrt.mongodb.net/?retryWrites=true&w=majority")
db = client["Test"]
collection = db.get_collection("users")
documents = collection.find()
lista = list(documents)

@app.route("/yield")
def test():
    # Get the next document from the database
    dicc = dict(collection.find_one_and_delete({}))
    obj_id = ObjectId(dicc['_id'])
    dicc['_id'] = str(obj_id)
    return dicc
    
    
    


if __name__ == "__main__":
    app.run()

  