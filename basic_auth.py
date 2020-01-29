from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth

from User import User
from errors import ApplicationError


def get_password_hash(password):
    return generate_password_hash(password)


def __verify_password(username, password):
    user = None
    try:
        user = User.find_by_username(username)
    except ApplicationError as err:
        if err.status_code != 404:
            raise err

    return user is not None and check_password_hash(user.password, password)


def init_basic_auth():
    auth = HTTPBasicAuth()
    auth.verify_password(__verify_password)
    return auth