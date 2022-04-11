from myapp.main import db
import json

class Customer(db.Model):
    ___tablename__ = 'customer' 

    id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String(50),nullable=False)
    last_name = db.Column(db.String(50),nullable=False)
    address = db.Column(db.String(500),nullable=False)
    city = db.Column(db.String(50),nullable=False)
    email = db.Column(db.String(50),nullable=False,unique=True)
    phone_number = db.Column(db.String(50),nullable=False)

    orders = db.relationship('Order',backref='customer')

    def json(self):
        return {
            'id':self.id,
            'first_name':self.first_name,
            'last_name':self.last_name,
            'address':self.address,
            'city':self.city,
            'email':self.email,
            'phone_number':self.phone_number
        }

    def __repr__ (self):
        return "<Customer '{}'>".format(self.first_name)
