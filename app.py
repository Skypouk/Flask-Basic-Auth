from flask import Flask, g
from flask_swagger_ui import get_swaggerui_blueprint
from decorators import deco
from auth import Auth
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    # generate token and put it in g.token
    print("verify password called...")
    token = Auth.encode_auth_token(username, password)
    g.token = token
    return True

SWAGGER_URL = '/doc'  # URL for exposing Swagger UI (without trailing '/')
API_URL = '/static/swagger.yml'  # Our API url (can of course be a local resource)

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Test application"
    },
    oauth_config = {  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
        #    'clientId': "your-client-id",
        #    'clientSecret': "your-client-secret-if-required",
        #    'realm': "your-realms",
        #    'appName': "your-app-name",
        #    'scopeSeparator': " ",
        #    'additionalQueryStringParams': {'test': "hello"}
    }
)

app.register_blueprint(swaggerui_blueprint)

@app.route("/request", methods=["GET"])
@auth.login_required
@deco
def get():
    # Your code to retrieve and return a list of items...
    res = {
        "data": "test"
    }
    return res, 200
app.run(debug=True)

# Now point your browser to localhost:5000/api/docs/