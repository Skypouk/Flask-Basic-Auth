from flask import make_response
from src.auth import Auth
from src.model import User


def check_basic_auth(username, password, required_scopes):
    try:
        return Auth.check_auth(username, password)
    except Exception:
        return


def post_user(body):
    try:
        User.add_user(body.get('username'), body.get('password'))
        return make_response(
            {
                "message": "User with username " +
                f"{body.get('username')} created successfully"
            },
            200
        )
    except Exception as exc:
        return make_response(
            {
                "error": str(exc),
            },
            500
        )


def get_data():
    res = {
        "data": "protected data"
    }
    return res, 200
