# Flask-Basic-Auth

## Project explanation

The project aim to create a Flask Api that uses Basic Authentification to restric access to some "Protected" endpoints.

The project uses openapi swagger to generate a user interface.

## How to use the API ?

To use the api, it only takes two steps:
  - Register in the API; by posting "username" and "password".
  - Access the protected data; by using the "Get" endpoint.

## Steps to setup the project:

### Install postgresql
### Create database with your chosen database name
### Setup .env file

Set values for variables SQLALCHEMY_DATABASE_URI and SALT by replacing {block} with your specific informations. 
SQLALCHEMY_DATABASE_URI = 'postgresql://{username}:{password}@localhost/{database_name}'
SALT = {generated_salt_for_encryption}

### Create and activate virtualenv
### Install requirements
```
pip install -r requirements.txt
```

# Setup migration
The command will create the "user" table.
```
flask --app src/app.py db upgrade
```

# Run the app
```
flask --app src/app.py run
```
