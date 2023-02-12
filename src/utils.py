import bcrypt
from dotenv import dotenv_values

config = dotenv_values(".env")


def encode_password(password):
    password = password.encode('utf-8')
    encrypted_password = bcrypt.hashpw(
        password, config.get('SALT').encode('utf-8')
    )

    return encrypted_password
