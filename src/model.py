import uuid
from . import db
from src.utils import encode_password
from sqlalchemy.exc import SQLAlchemyError


class User(db.Model):
    user_id = db.Column(db.String(100), primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)

    def __init__(self, username, password):
        self.user_id = uuid.uuid4()
        self.username = username
        self.password = password

    @staticmethod
    def add_user(username, password):
        try:
            encrypted_password = encode_password(password)
            new_user = User(username, encrypted_password.decode('utf-8'))
            db.session.add(new_user)
            db.session.commit()
        except SQLAlchemyError:
            raise Exception("Username already exists")
        except Exception:
            raise Exception("Error while adding the user")

    @staticmethod
    def get_user(username):
        try:
            user = db.session.query(User).filter(
                User.username == username
            ).first()
            return user
        except Exception as exc:
            raise Exception(f"Error while retrieving the user {str(exc)}")

    def __repr__(self):
        return f"User user_id:{self.user_id},\
                 username:{self.username}, \
                 password:{self.password}"
