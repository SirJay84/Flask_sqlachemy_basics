from customer import *

def create_customer(_first_name,_last_name,_address,_city,_email,_phone_number):
    new_customer = Customer(
            first_name=_first_name,
            last_name=_last_name,
            address=_address,
            city=_city,
            email=_email,
            phone_number=_phone_number
        )
    db.session.add(new_customer)
    db.session.commit()

def get_all_customers():
    customers = Customer.query.all()
    customer_list = []
    for customer in customers:
        customer_details = {
            'first_name':customer.first_name,
            'last_name':customer.last_name,
            'address':customer.address,
            'city':customer.city,
            'email':customer.email,
            'phone_number':customer.phone_number
        }
        customer_list.append(customer_details)
    return {'customers':customer_list}

def get_one_customer(_id):
    customer = Customer.query.filter_by(id=_id).first()
    customer_details = {
            'first_name':customer.first_name,
            'last_name':customer.last_name,
            'address':customer.address,
            'city':customer.city,
            'email':customer.email,
            'phone_number':customer.phone_number
        }
    return {'customer':customer_details}

def update_customer(_id,_first_name,_last_name,_address,_city,_email,_phone_number):
    customer = Customer.query.filter_by(id=_id).first()
    customer.first_name = _first_name
    customer.last_name = _last_name
    customer.address = _address
    customer.city = _city
    customer.email = _email
    customer.phone_number = _phone_number
    db.session.commit()
    
def delete_customer(_id):
    customer = Customer.query.filter_by(id=id).first()
    db.session.delete(customer)
    db.session.commit()
    
