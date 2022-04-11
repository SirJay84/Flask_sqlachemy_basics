from flask import request,Response
from order_service import *

@app.route('/order', methods=['POST'])
def create_order():
    request_data = request.get_json()
    Order.create_order(
        request_data['order_date'],
        request_data['shipped_date'],
        request_data['delivered_date'],
        request_data['coupon_code'],
        request_data['customer_id']
    )
    response = Response('Order created',status=201,mimetype='application/json')
    return response

@app.route('/order', methods=['GET'])
def get_all_orders():
    orders = Order.query.all()
    return orders

@app.route('/order/<int:id>', methods=['GET'])
def get_an_order(id):
    order = Order.query.filter_by(id=id).first()
    return order

@app.route('/order/<int:id>', methods=['PUT'])
def update_order(id):
    request_data = request.get_json()
    Order.update_order(
        id,
        request_data['order_date'],
        request_data['shipped_date'],
        request_data['delivered_date'],
        request_data['coupon_code'],
        request_data['customer_id']
    )
    response = Response('Order updated',status=200,mimetype='application/json')
    return response

@app.route('/order/<int:id>', methods=['DELETE'])
def delete_order(id):
    Order.delete_order(id)
    response = Response('Order deleted',status=200,mimetype='application/json')
    return response