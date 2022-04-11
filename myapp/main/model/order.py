from myapp.main import db
from datetime import datetime
import json

order_product = db.Table(
    'order_product',
    db.Column('order_id',db.Integer,db.ForeignKey('order.id'),primary_key=True),
    db.Column('product_id',db.Integer,db.ForeignKey('product.id'),primary_key=True)    
)

class Order(db.Model):
    ___tablename__ = 'order'

    id = db.Column(db.Integer,primary_key=True)
    order_date = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    shipped_date = db.Column(db.DateTime)
    delivered_date = db.Column(db.DateTime)
    coupon_code = db.Column(db.String(50))
    
    customer_id = db.Column(db.Integer,db.ForeignKey('customer.id'),nullable=False)

    products = db.relationship('Product',secondary=order_product)

    def json(self):
        return {
            'id':self.id,
            'order_date':self.order_date,
            'shipped_date':self.shipped_date,
            'delivered_date':self.delivered_date,
            'coupon_code':self.coupon_code,
            'customer_id':self.customer_id
        }
    
    def __repr__ (self):
        return "<Order '{}'>".format(self.id)

        