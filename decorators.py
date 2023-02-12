from flask import g
from auth import Auth
from functools import wraps
from flask import request


def deco(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            # check if token exist, check his validity
            auth = request.authorization
            user = Auth.has_auth(auth.password)
        except Exception as exc:
            return {
                "error": str(exc),
            }, 401
        return func(*args, **kwargs)
    return wrapper