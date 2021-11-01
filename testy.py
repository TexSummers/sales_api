order_products = db.Table('order_products',
                          db.Column('order_id', db.Integer, db.ForeignKey('orders.id')),
                          db.Column('product_id', db.Integer, db.ForeignKey('products.id'))
                          db.Column('product_qty', db.Integer)
                          )