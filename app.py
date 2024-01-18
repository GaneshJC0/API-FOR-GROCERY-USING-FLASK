from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)


class Grocery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(120), unique=True, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    customer_rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"{self.item} - {self.price} - {self.quantity} - {self.customer_rating}"

@app.route('/')
def index():
    return "Hello, Welcome to MyMart Shopping"


@app.route('/Groceries', methods=['GET', 'POST'])
def get_groceries():
    if request.method == 'GET':
        groceries = Grocery.query.all()
        grocery_list = [
            {'id': grocery.id, 'items': grocery.item, 'price': grocery.price, 'quantity': grocery.quantity,
             'customer_rating': grocery.customer_rating} for grocery in groceries]
        return jsonify(grocery_list)
    elif request.method == 'POST':
        data = request.get_json()
        new_item = data.get('item')
        new_price = data.get('price')
        new_quantity = data.get('quantity')
        new_customer_rating = data.get('customer_rating')

        new_grocery = Grocery(item=new_item, price=new_price, quantity=new_quantity,
                              customer_rating=new_customer_rating)
        db.session.add(new_grocery)
        db.session.commit()

        print(f'Received new grocery {new_grocery}')
        return jsonify({'id': new_grocery.id, 'items': new_grocery.item, 'price': new_grocery.price, 'quantity': new_grocery.quantity,
                        'customer_rating': new_grocery.customer_rating})


@app.route('/Groceries/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def get_or_update_grocery(id):
    grocery = Grocery.query.get(id)

    if request.method == 'GET':
        if grocery:
            grocery_data = {'id': grocery.id, 'item': grocery.item, 'price': grocery.price, 'quantity': grocery.quantity,
                            'customer_rating': grocery.customer_rating}
            return jsonify(grocery_data)
        else:
            return "Grocery Not Found", 404

    elif request.method == 'PUT':
        data = request.get_json()
        grocery.item = data.get('item', grocery.item)
        grocery.price = data.get('price', grocery.price)
        grocery.quantity = data.get('quantity', grocery.quantity)
        grocery.customer_rating = data.get('customer_rating', grocery.customer_rating)
        db.session.commit()
        return jsonify({'message': 'Grocery updated successfully'})

    elif request.method == 'DELETE':
        db.session.delete(grocery)
        db.session.commit()
        return jsonify({'message': 'Grocery deleted successfully'})

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
