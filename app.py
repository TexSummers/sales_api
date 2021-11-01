import classes
from classes import *


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/customers', methods=['GET'])
def get_all_customers():
    return jsonify({'Customers': classes.get_all_customers()})


@app.route('/customers/<int:_id>', methods=['GET'])
def get_customer(_id):
    return_value = classes.get_customer(_id)
    return jsonify(return_value)


@app.route('/customers', methods=['POST'])
def add_customer():
    request_data = request.get_json()
    classes.add_customer(request_data["first_name"], request_data["last_name"])
    response = Response("Customer added!", 201, mimetype='application/json')
    return response


@app.route('/customers/<int:id>', methods=['DELETE'])
def remove_customer(_id):
    classes.delete_customer(_id)
    response = Response("Customer deleted!", status=200, mimetype='application/json')
    return response


@app.route('/orders', methods=['GET'])
def get_all_orders():
    return jsonify({'Orders': classes.get_all_orders()})


@app.route('/orders/<int:_id>', methods=['GET'])
def get_order(_id):
    return_value = classes.get_order(_id)
    return jsonify(return_value)


@app.route('/orders', methods=['POST'])
def add_order():
    request_data = request.get_json()
    classes.add_order(request_data['customer_id'], request_data['products'], request_data['total'])
    response = Response("Order added!", 201, mimetype='application/json')
    return response


@app.route('/orders/<int:id>', methods=['DELETE'])
def remove_order(_id):
    classes.delete_order(_id)
    response = Response("Order deleted!", status=200, mimetype='application/json')
    return response


@app.route('/products', methods=['GET'])
def get_products():
    return jsonify({'Products': classes.get_all_products()})


@app.route('/products/<string:product_name>', methods=['GET'])
def get_product_by_name(product_name):
    return_value = classes.get_product_by_name(product_name)
    return jsonify(return_value)


@app.route('/products/<int:_id>', methods=['GET'])
def get_product_by_id(_id):
    return_value = classes.get_product(_id)
    return jsonify(return_value)


@app.route('/products', methods=['POST'])
def add_product():
    request_data = request.get_json()
    classes.add_product(request_data["name"], request_data["price"], request_data["stock"])
    response = Response("Product added!", 201, mimetype='application/json')
    return response


@app.route('/products/<int:id>', methods=['DELETE'])
def remove_products(_id):
    classes.delete_product(_id)
    response = Response("Product deleted!", status=200, mimetype='application/json')
    return response


if __name__ == "__main__":
    app.run(debug=True)
