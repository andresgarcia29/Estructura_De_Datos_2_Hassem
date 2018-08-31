from functools import wraps
from flask import request
from contracts.validations import validate_permission


def get_secret_role(name):
    def get_secret_role(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if validate_permission(name, request.headers.get('auth')):
                return f(**kwargs)
            raise("You don't have this permission")
        return decorated_function
    return get_secret_role
