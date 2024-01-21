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
    return str(backend.get_orderbook())

def get_order_book_by_user_id(user_id):  # noqa: E501
    """Get top 10 unfulfilled buy and sell orders by user id

    Get order book by user id # noqa: E501

    :param user_id: User ID
    :type user_id: str

    :rtype: List[Order]
    """

    return str(backend.get_orderbook(10, user_id))

def get_user_pnl(user_id):  # noqa: E501
    """Get user pnl

    Get user pnl # noqa: E501

    :param user_id: User ID
    :type user_id: str

    :rtype: float
    """
    user = backend.get_user(user_id)
    if user is None:
        return "User not found", 404
    return backend.user_expected_pnl(user)


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
        body = connexion.request.get_json()  # noqa: E501
    print(body, file=sys.stdout)
    user = user_id
    type = body["type"]
    price = int(body["price"])
    quantity = int(body["quantity"])
    try:
        backend.add_order(user, type, price, quantity)
    except Exception as e:
        print(e, file=sys.stdout)
        return str(e), 400
    return '200'

def get_results():  # noqa: E501
    """Get results

    Get results # noqa: E501


    :rtype: str
    """
    return backend.leaderboard(10)

def get_all_users():  # noqa: E501
    """Get all users

    Get all users # noqa: E501


    :rtype: List[User]
    """
    return backend.get_all_users()
