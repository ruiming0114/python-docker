from flask import Flask, request, jsonify
from random import *

app = Flask(__name__)

#get请求——query参数———返回String
@app.route('/api/hello')
def hello_world():
    return "hello, "+request.args.get('name')+"!"

#get请求——query参数———返回String
@app.route('/api/random', methods=["POST"])
def random_number():
    if request.method == 'POST':
        response = {
            "name": "Lord " + request.form.get('name'),
            'randomNumber': randint(1, 100)
        }
        return jsonify(response)

#get请求——query参数———返回String
@app.route('/api/addPrice', methods=["PUT"])
def add_price():
    if request.method == 'PUT':
        data = request.get_json()
        sum =0
        for item in data:
            sum+=item['price']
        return jsonify({"total": sum})



