from flask import Flask, request, jsonify
from sql_connection import get_sql_connection
#import _mysql_connector
import product_dao
import uom_dao
import json
import orders_dao

app = Flask(__name__)    #This line initializes the Flask application by creating an instance of the Flask class.

connection = get_sql_connection()   #function to establish a connection to the database

@app.route('/getProducts', methods=['GET'])
def get_products():
    products = product_dao.get_all_products(connection)
    response =  jsonify(products)    #The jsonify function converts the list of products into a JSON response that can be returned to the client 
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/getUOM', methods=['GET'])
def get_uom():
    response = uom_dao.get_uoms(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    return_id = product_dao.delete_product(connection, request.form['products_id'])
    response = jsonify({
        'product_id': return_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/insertProduct', methods=['POST'])
def insert_product():
    request_payload = json.loads(request.form['data'])
    products_id = product_dao.insert_new_product(connection, request_payload)
    response = jsonify({
        'product_id': products_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getAllOrders', methods=['GET'])
def get_all_orders():
    response = orders_dao.get_all_orders(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertOrder', methods=['POST'])
def insert_order():
    request_payload = json.loads(request.form['data'])
    order_id = orders_dao.insert_order(connection, request_payload)
    response = jsonify({
        'order_id': order_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Grocery Store Management System")
    app.run(port=5000)
