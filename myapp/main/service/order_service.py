from order import *

def create_order(_order_date,_shipped_date,_delivered_date,_coupon_code,_customer_id):
    new_order = Order(
        order_date = _order_date,
        shipped_date = _shipped_date,
        delivered_date = _delivered_date,
        coupon_code = _coupon_code,
        customer_id = _customer_id
    )
    db.session.add(new_order)
    db.session.commit()

def get_all_orders():
    orders = Order.query.all()
    order_list = []
    for order in orders:
        order_details = {
            'order_date':datetime.utcnow,
            'shipped_date':datetime.utcnow,
            'delivered_date':datetime.utcnow,
            'coupon_code':order.coupon_code,
            'customer_id':order.customer_id
        }
        order_list.append(order_details)
    return {'orders':order_list}

def get_an_order(_id):
    order = Order.query.filter_by(id=_id).first()
    order_details = {
            'order_date':datetime.utcnow,
            'shipped_date':datetime.utcnow,
            'delivered_date':datetime.utcnow,
            'coupon_code':order.coupon_code,
            'customer_id':order.customer_id
        }
    return {'order':order_details}

def update_order(_id,_order_date,_shipped_date,_delivered_date,_coupon_code,_customer_id):
    order = Order.query.filter_by(id=_id).first()
    order.order_date = _order_date
    order.shipped_date = _shipped_date
    order.delivered_date = _delivered_date
    order.coupon_code = _coupon_code
    order.customer_id = _customer_id
    db.session.commit()

def delete_order(_id):
    order = Order.query.filter_by(id=_id).first()
    db.session.delete(order)
    db.session.commit()  

    