from flask import request,Response
from product_service import * 

@app.route('/product', methods=['POST'])
def create_product():
    request_data = request.get_json()
    Product.create_product(request_data['name'],request_data['price'])
    response = Response('Product created',status=201,mimetype='application/json')
    return response

@app.route('/product', methods=['GET'])
def get_all_products():
    products = Product.query.all()
    return products 

@app.route('/product/<int:id>', methods=['GET'])
def get_one_product(id):
    product = Product.query.filter_by(id=id).first()
    return product 

@app.route('/product/<int:id>', methods=['PUT'])
def update_product(id):
    request_data = request.get_json()
    Product.update_product(id,request_data['name'],request_data['price'])
    response = Response('Product updated',status=200,mimetype='application/json')
    return response

@app.route('/product/<int:id>', methods=['DELETE'])
def delete_product(id):
    Product.delete_product(id)
    response = Response('Product deleted',status=200,mimetype='application/json')
    return response