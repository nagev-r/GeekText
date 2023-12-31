from flask import Flask, request, jsonify
from flask import Blueprint
from Main.geektext.ShoppingCart.ShoppingCartRepository import ShoppingCartRepository
from Main.geektext.resources.DataAccess import db_connection


repository = ShoppingCartRepository(db_connection)

shoppingcart = Blueprint('shoppingcart', __name__, url_prefix='/shoppingcart')

@shoppingcart.route('/calculate_subtotal', methods=['GET'])
def calculate_subtotal():
    # calculates and retrieves the subtotal in the user's shopping cart
    user_id = request.json.get('user_id')  # get the user_id from the request query parameters
    subtotal = repository.get_subtotal(user_id)  # use the repository to get the subtotal
    return jsonify({"subtotal": subtotal})  # return the subtotal as JSON

@shoppingcart.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    # add book to user's shopping cart
    user_id = request.json.get('user_id')
    isbn = request.json.get('isbn')  # Assuming the ISBN is sent in the request body as JSON
    repository.add_item_to_cart(isbn, user_id)
    return "Item added to the cart", 201  # HTTP 201 for resource created

@shoppingcart.route('/get_cart_items', methods=['GET'])
def get_cart_items():
    # retrieves items in the user's shopping cart with book details
    user_id = request.args.get('user_id')
    cart_items = repository.get_cart_items(user_id)
    return jsonify({"cart_items": cart_items})  # return the cart items as JSON
@shoppingcart.route('/delete_from_cart', methods=['DELETE'])
def delete_from_cart():
    # removes book from user's shopping cart
    user_id = request.args.get('user_id')
    isbn = request.args.get('isbn')
    repository.delete_item_from_cart(isbn, user_id)
    return "Item removed from the cart", 204  # HTTP 204 for resource removed
