from product import *

def create_product(_name,_price):
    new_product = Product(name=_name,price=_price)
    db.session.add(new_product)
    db.session.commit()

def get_all_products():
    products = Product.query.all()
    product_list = []
    for product in products:
        product_details = {'name':product.name,'price':product.price}
        product_list.append(product_details)
    return {'products':product_list}

def get_one_product(_id):
    product = Product.query.filter_by(id=_id).first()
    product_details = {'name':product.name,'price':product.price}
    return {'product':product_details}

def update_product(_id,_name,_price):
    product = Product.query.filter_by(id=_id).first()
    product.name = _name
    product.price = _price
    db.session.commit()

def delete_product(_id):
    product = Product.query.filter_by(id=_id).first()
    db.session.delete(product)
    db.session.commit()

