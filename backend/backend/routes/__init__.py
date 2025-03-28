import jwt

from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from werkzeug.security import generate_password_hash, check_password_hash

allowed_users = {
    "longwei": generate_password_hash("my-password"),
    "bob": generate_password_hash("his-password"),
    }

allowed_tokens = {
    "token-longwei": "longwei",
    "token-bob": "bob",
    }

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth(scheme="Bearer")

secret_token = "mysecret"

@basic_auth.verify_password
def verify_basic_password(username, password):
    if username not in allowed_users:
        return None

    if check_password_hash(allowed_users[username], password):
        return username

@token_auth.verify_token
def verify_token(token):
    try:
        decoded_jwt = jwt.decode(token, secret_token, algorithms=["HS256"])
    except Exception as e:
        print(e)
        return None
    if decoded_jwt["name"] in allowed_users:
        print('name', decoded_jwt["name"])
        return decoded_jwt["name"]
    return None