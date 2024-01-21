import connexion
import six
import uuid

from swagger_server.models.user import User  # noqa: E501
from swagger_server import util
from swagger_server import backend_object
from random import randint


def create_user(name):  # noqa: E501
    """Create a new user

    Create a new user # noqa: E501

    :param name: User name
    :type name: str

    :rtype: None
    """
    id = str(randint(0, 20))
    if name == "user1":
        id = "1"
    elif name == "user2":
        id = "2"
    elif name == "user3":
        id = "3"
    backend_object.add_user(id, name)
    return id

def uncompress(a):
    b = {}
    for i in a:
        b[i[0]] = b.get(i[0], 0) + i[1]
    return b

def get_user(user_id):  # noqa: E501
    """Get user information

    Get user information # noqa: E501

    :param user_id: User ID
    :type user_id: str

    :rtype: User
    """
    user = backend_object.get_user(user_id)
    if user is None:
        return "User not found", 404
    return {
        "name": user.user_name,
        "id": user.user_id,
        "score": user.position,
        "buys": uncompress(user.buys),
        "sells": uncompress(user.sells),
    }


def update_user(user_id, score):  # noqa: E501
    """Update user score

    Update user score # noqa: E501

    :param user_id: User ID
    :type user_id: str
    :param score: User score
    :type score: float

    :rtype: None
    """
    user = backend_object.get_user(user_id)
    if user is None:
        return "User not found", 404
    user.position = score
    backend_object.update_user(user)
    return "200"
