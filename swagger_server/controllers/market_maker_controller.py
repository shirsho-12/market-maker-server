import connexion
import six

from swagger_server.models.order import Order  # noqa: E501
from swagger_server import util


def get_order_book():  # noqa: E501
    """Get top 10 unfulfilled buy and sell orders

    Get order book # noqa: E501


    :rtype: List[Order]
    """
    return 'do some magic!'


def place_order(body, user_id):  # noqa: E501
    """Place an order

    Place an order in the market # noqa: E501

    :param body: Order Information
    :type body: dict | bytes
    :param user_id: User ID
    :type user_id: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Order.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
