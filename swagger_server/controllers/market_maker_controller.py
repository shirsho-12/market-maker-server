import connexion
import six

from swagger_server.models.order import Order  # noqa: E501
from swagger_server import util

# get backend object
from swagger_server import backend_object as backend
import logging
import sys

def get_order_book():  # noqa: E501
    """Get top 10 unfulfilled buy and sell orders

    Get order book # noqa: E501


    :rtype: List[Order]
    """
    return backend.get_orderbook()


def place_order(body, user_id):  # noqa: E501
    """Place an order

    Place an order in the market # noqa: E501

    :param body: Order Information
    :type body: dict | bytes
    :param user_id: User ID
    :type user_id: str

    :rtype: None
    """
    print("place order", file=sys.stdout)
    if connexion.request.is_json:
        body = Order.from_dict(connexion.request.get_json())  # noqa: E501
    print(body, file=sys.stdout)
    user = user_id
    type = body["type"]
    price = body["price"]
    quantity = body["quantity"]
    try:
        backend.add_order(user, type, price, quantity)
    except Exception as e:
        return str(e), 400
    return '200'
