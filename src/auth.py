import bcrypt
from src.model import User
import datetime


class Auth:
    @staticmethod
    def check_auth(username, password):
        password = password.encode('utf-8')

        user = User.get_user(username)
        stored_password = user.password.encode('utf-8')

        if bcrypt.checkpw(password, stored_password):
            return {
                'sub': user.user_id,
                'name': username,
                'iat': datetime.datetime.now().timestamp()
            }
