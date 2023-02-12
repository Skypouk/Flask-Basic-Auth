import connexion
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from dotenv import dotenv_values

config = dotenv_values(".env")
db = SQLAlchemy()


def create_app():
    connexion_app = connexion.FlaskApp(__name__, specification_dir='./static/')
    connexion_app.add_api('swagger.yml')
    app = connexion_app.app

    app.config['SQLALCHEMY_DATABASE_URI'] = config.get(
        'SQLALCHEMY_DATABASE_URI'
    )
    db.init_app(app)

    Migrate(app, db)

    return app
