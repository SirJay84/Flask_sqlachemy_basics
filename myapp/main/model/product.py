from myapp.main import db
import json

class Product(db.Model):
    ___tablename__ = 'product'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50),nullable=False,unique=True)
    price = db.Column(db.Integer,nullable=False)

    def json(self):
        return {'id':self.id,'name':self.name,'price':self.price}
    
    def __repr__ (self):
        return "<Product '{}'>".format(self.id)