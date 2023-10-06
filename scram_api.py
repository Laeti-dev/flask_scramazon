from flask import Flask, jsonify
import sqlite3 as sql
import pandas as pd


# Create flask app
app = Flask(__name__)

# Function to access db
def request_db(query, db="scram.db"):
    with sql.connect(db) as db:
        res = pd.read_sql(query, db)
        return res.to_json(orient="records")

@app.route("/products")
def get_products():
    query = '''SELECT DISTINCT  Name
FROM  Product'''
    res = request_db(query)
    return res

@app.route("/maincat")
def get_maincats():
    query = '''SELECT DISTINCT  id, Name
FROM  MainCategory'''
    res = request_db(query)
    return res

@app.route("/subcat")
def get_subcats():
    query = '''SELECT DISTINCT  id, Name
FROM  SubCategory'''
    res = request_db(query)
    return res

# @app.route("/addProduct", methods=["POST"])
# def add_product():
#     query =


# Run app
if __name__ == '__main__':
    app.run()
