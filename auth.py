from flask import g
from jwt import (
    JWT,
    jwk_from_dict,
    jwk_from_pem,
)
from jwt.utils import get_int_from_datetime
import datetime

instance = JWT()
SECRET_KEY = None
with open('rsa_private_key.pem', 'rb') as fh:
    SECRET_KEY = jwk_from_pem(fh.read())


class Auth:
    @staticmethod
    def has_auth(password):
        try:
            if hasattr(g, 'token'):
                #if password == Auth.decode_auth_token(g.token):
                #    return
                print(Auth.decode_auth_token(g.token))
                #else:
                #    raise Exception("Invalid token")

            raise Exception("Not autheticated")
        except Exception as exc:
            raise exc

    @staticmethod
    def encode_auth_token(username, password):
        """
        Generates the Auth Token
        :return: string
        """
        print("encode token called")
        try:
            payload = {
                'exp': get_int_from_datetime(datetime.datetime.utcnow() + datetime.timedelta(minutes=30)),
                'iat': get_int_from_datetime(datetime.datetime.utcnow()),
                'sub': password,
            }
            return instance.encode(
                payload,
                SECRET_KEY,
                alg='RS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        print("decode token called")
        try:
            payload = instance.decode(auth_token, SECRET_KEY, do_time_check=True)
            return payload['sub']
        except Exception as e:
            if 'Invalid token' in str(e):
                print("Token is invalid.")
            else:
                print("An error occurred:", e)

        
