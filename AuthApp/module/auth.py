from flask import jsonify, request
from AuthApp.models import User
from functools import wraps
import jwt
import os
import datetime
from settings.extension import db
from werkzeug.security import check_password_hash, generate_password_hash
from settings.response import TokenType
from AuthApp.module.email import EmailService

SECRET_KEY = os.environ.get('SECRET_KEY')


# decorator for verifying the JWT access token
def RequiredAuthToken(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
            token = token.split(' ')[1]
        # return 401 if token is not passed
        if not token:
            return jsonify({'message': 'Token is missing !!'}), 401

        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(token, SECRET_KEY, 'utf-8')
            current_user = User.query \
                .filter_by(id=data['user_id'], is_active=True, is_verify=True, is_delete=False) \
                .first()
        except jwt.ExpiredSignatureError:
            return jsonify({
                'message': 'Token is expired !!'
            }), 401
        except jwt.InvalidTokenError:
            return jsonify({
                'message': 'Token is invalid !!'
            }), 401
        # returns the current logged in users contex to the routes
        return f(current_user, *args, **kwargs)

    return decorated


def GetJwtToken(data, tokenTime):
    value = tokenTime.get('value')
    if tokenTime.get('type') == TokenType.accessToken.value:
        payload = {'user_id': data.id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=value)}
    else:
        payload = {'user_id': data.id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(days=value)}
    token = jwt.encode(payload, SECRET_KEY).decode('utf-8')
    # result = json.dumps({"access_token": str(token)})
    return token


# Create user method
def createUser(data):
    # Extract data from data
    firstName = data['firstName']
    lastName = data['lastName']
    userName = data['userName']
    email = data['email']
    mobile = int(data['mobile'])
    password = data['password']

    # Generate password hash
    password = generate_password_hash(password)
    dateTime = str(datetime.datetime.timestamp(datetime.datetime.now()))

    # Save data into model
    obj = User(first_name=firstName, last_name=lastName, username=userName, email=email, mobile=mobile, password=password,
               created_on=dateTime, updated_on=dateTime)
    db.session.add(obj)
    db.session.commit()

    email = EmailService()
    email.saveEmail(obj)

    return obj


# Login User
def loginUser(data):
    email = data['email']
    password = data['password']
    userObj = User.query.filter_by(email=email, is_active=True, is_verify=True, is_delete=False).first()
    if userObj is not None and check_password_hash(userObj.password, password):
        result = {
            "canLogin": True,
            "data": userObj.id
        }
    else:
        result = {
            "canLogin": False,
            "data": userObj.id
        }
    return result
