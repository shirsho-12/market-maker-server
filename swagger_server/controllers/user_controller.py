import connexion
import six

from swagger_server.models.user import User  # noqa: E501
from swagger_server import util


def create_user(name):  # noqa: E501
    """Create a new user

    Create a new user # noqa: E501

    :param name: User name
    :type name: str

    :rtype: None
    """
    return 'do some magic!'


def get_user(user_id):  # noqa: E501
    """Get user information

    Get user information # noqa: E501

    :param user_id: User ID
    :type user_id: str

    :rtype: User
    """
    return 'do some magic!'


def update_user(user_id, score):  # noqa: E501
    """Update user score

    Update user score # noqa: E501

    :param user_id: User ID
    :type user_id: str
    :param score: User score
    :type score: float

    :rtype: None
    """
    return 'do some magic!'
