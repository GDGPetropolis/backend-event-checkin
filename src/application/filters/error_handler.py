from functools import wraps
from flask import Response


def error_handler(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as ex:
            print(ex)
            return Response(status=500)

    return decorated_function
