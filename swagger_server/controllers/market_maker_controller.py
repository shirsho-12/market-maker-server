import connexion
import six

from swagger_server.models.order import Order  # noqa: E501
from swagger_server import util


def place_order(userId, order):  # noqa: E501
    """Place an order

    Place an order in the market # noqa: E501

    :param userId: User ID
    :type userId: str
    :param order: Order Information
    :type order: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        order = Order.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
