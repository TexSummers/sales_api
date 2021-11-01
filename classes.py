from config import *

order_products = db.Table('order_products',
                          db.Column('order_id', db.Integer, db.ForeignKey('orders.id')),
                          db.Column('product_id', db.Integer, db.ForeignKey('products.id')),
                          db.Column('product_qty', db.Integer)
                          )


class Customers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    orders = db.relationship('Orders', backref='customer')

    def json(self):
        return {'id': self.id, 'first_name': self.first_name, 'last_name': self.last_name}
        # " 'orders': self.orders "... goes where?


def add_customer(first, last):
    new_customer = Customers(first_name=first, last_name=last)
    db.session.add(new_customer)
    db.session.commit()


def get_all_customers():
    return [Customers.json(customer) for customer in Customers.query.all()]


# How to implement first AND last name in URL routing?
def get_customer_by_name(first_name, last_name):
    return [Customers.json(Customers.query.filter_by(first_name=first_name, last_name=last_name).first_or_404())]


def get_customer(_id):
    return [Customers.json(Customers.query.filter_by(id=_id).first_or_404())]


def delete_customer(_id):
    Customers.query.filter_by(id=_id).delete()
    db.session.commit()


class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    products = db.relationship('Products', secondary=order_products, backref=db.backref('in_order', lazy='dynamic'))
    total = db.Column(db.Integer)

    def json(self):
        return {'id': self.id, 'customer_id': self.customer_id, 'products': self.products, 'total': self.total}


def add_order(customer_id, products, total):
    new_order = Orders(customer_id=customer_id, products=products, total=total)
    db.session.add(new_order)
    db.session.commit()


def get_all_orders():
    return [Orders.json(order) for order in Orders.query.all()]


def get_order(_id):
    return [Orders.json(Orders.query.filter_by(id=_id).first_or_404())]


def delete_order(_id):
    Orders.query.filter_by(id=_id).delete()
    db.session.commit()


class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(80))
    price = db.Column(db.Integer)
    stock = db.Column(db.Integer)

    def json(self):
        return {'id': self.id, 'product_name': self.product_name, 'price': self.price, 'stock': self.stock}


def add_product(name, price, stock):
    new_product = Products(name=name, price=price, stock=stock)
    db.session.add(new_product)
    db.session.commit()


def get_all_products():
    return [Products.json(product) for product in Products.query.all()]


def get_product_by_name(product_name):
    return [Products.json(Products.query.filter_by(product_name=product_name).first_or_404())]


def get_product(_id):
    return [Products.json(Products.query.filter_by(id=_id).first_or_404())]


def delete_product(_id):
    Products.query.filter_by(id=_id).delete()
    db.session.commit()
