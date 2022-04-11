from flask import request,Response
from customer_service import *

@app.route('/customer', methods=['POST'])
def create_customer():
    request_data = request.get_json()
    Customer.create_customer(
        request_data['first_name'],
        request_data['last_name'],
        request_data['address'],
        request_data['city'],
        request_data['email'],
        request_data['phone_number']
    )
    response = Response('Customer created',status=201,mimetype='application/json')
    return response

@app.route('/customer', methods=['GET'])
def get_all_customers():
    customers = Customer.query.all()
    return customers

@app.route('/customer/<int:id>', methods=['GET'])
def get_one_customer(id):
    customer = Customer.query.filter_by(id=id).first()
    return customer

@app.route('/customer/<int:id>', methods=['PUT'])
def update_customer(id):
    request_data = request.get_json()
    Customer.update_customer(
        id,
        request_data['first_name'],
        request_data['last_name'],
        request_data['address'],
        request_data['city'],
        request_data['email'],
        request_data['phone_number']
    )
    response = Response('Customer updated',status=200,mimetype='application/json')
    return response

@app.route('/customer/<int:id>' , methods=['DELETE'])
def delete_customer(id):
    Customer.delete_customer(id)
    response = Response('Customer deleted',status=200,mimetype='application/json')
    return response
    
