from myapp.main import *
from myapp.main.model.customer import Customer
from myapp.main.model.order import order_product
from myapp.main.model.order import Order
from myapp.main.model.product import Product
from faker import Faker
import random
from datetime import datetime,timedelta

fake = Faker()

def add_customers():
    # loop over 100 times to create customer
    for _ in range(100):
        customer = Customer(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            address =fake.address(),
            city =fake.city(),
            email =fake.email(),
            phone_number =fake.phone_number()
        )
        db.session.add(customer)
    db.session.commit()

def add_orders():
    customers = Customer.query.all()
    
    # loop over 1000 times to create an order
    for _ in range(1000):
        # choose a random customer
        customer = random.choice(customers)
        
        # choose either random None or random order_date & shipped_date
        order_date = fake.date_time_this_year()
        shipped_date = random.choices([None,fake.date_time_between(start_date=order_date)],[10,90])[0]
        
        # choose either random None or random shipped_date & delivered_date
        delivered_date = None
        if shipped_date:
            delivered_date = random.choices([None,fake.date_time_between(start_date=shipped_date)],[50,50])[0]
        
        # choose either random None or one of the three coupon codes
        coupon_code = random.choices([None,'50OFF','FREESHIPPING','BUYONEGETONE'],[85,5,5,5])[0]
        
        order = Order(
            order_date=order_date,
            shipped_date=shipped_date,
            delivered_date=delivered_date,
            coupon_code=coupon_code,
            customer_id=customer.id
        )
        db.session.add(order)
    db.session.commit()

def add_products():
    # loop over 10 times to create product
    for _ in range(10):
        product = Product(
            name=fake.color_name(),
            price=random.randint(10,100)
        )
        db.session.add(product)
    db.session.commit()

def add_order_product():
    orders = Order.query.all()
    products = Product.query.all()

    for order in orders:
        # select random k
        k = random.randint(1,3)
        
        # select random products
        purchased_products = random.sample(products,k)
        order.products.extend(purchased_products)

    db.session.commit()

def create_random_data():
    db.create_all()
    add_customers()
    add_orders()
    add_products()
    add_order_product()

def get_orders_by(customer_id=1):
    print('Get orders by customer')
    customer_orders = Order.query.filter_by(customer_id=customer_id).all()
    for order in customer_orders:
        print(order.order_date)

def get_pending_orders():
    print('Pending orders')
    pending_orders = Order.query.filter(Order.shipped_date.is_(None)).all()
    for order in pending_orders:
        print(order.order_date)

def get_pending_orders():
    print('Pending orders')
    pending_orders = Order.query.filter(Order.shipped_date.is_(None)).order_by(Order.order_date.desc()).all()
    for order in pending_orders:
        print(order.order_date)

def how_many_customers():
    print('how many customers?')
    print(Customer.query.count())

def orders_with_coupon_codes():
    print('Orders with coupon_codes')
    orders = Order.query.filter(Order.coupon_code.isnot(None)).all()
    for order in orders:
        print(order.coupon_code)

def orders_with_coupon_codes():
    print('Orders with coupon_codes')
    orders = Order.query.filter(Order.coupon_code.isnot(None)).filter(Order.coupon_code !='FREESHIPPING').all()
    for order in orders:
        print(order.coupon_code)

def revenue_past_x_days(x_days=30):
    print('Revenue past x days')
    print(db.session
        .query(db.func.sum(Product.price))
        .join(order_product).join(Order)
        .filter(Order.order_date > (datetime.now()- timedelta(days=x_days))).scalar()
    )

def average_fulfillment_time():
    print('Average fulfillment time')
    print(
        db.session.query(
            db.func.time(
                db.func.avg(
                    db.func.strftime('%s',Order.shipped_date) - db.func.strftime('%s', Order.order_date)
                ),
                'unixepoch'
            )
        ).filter(Order.shipped_date.isnot(None)).scalar()
    )

def get_customers_who_have_purchased_x_dollars(amount=500):
    print('Get customers who have purchased x dollars')
    customers = db.session.query(Customer).join(Order).join(order_product).join(Product).group_by(Customer).having(db.func.sum(Product.price) > amount).all()
    for customer in customers:
        print(customer.first_name)




