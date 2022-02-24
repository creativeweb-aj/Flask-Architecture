import json
from flask import Blueprint, Response, request
from flasgger.utils import swag_from
from settings.response import TokenType, StatusType, ResponseModal
from apps.AuthApp.schema import UserSchema, User
from apps.AuthApp.module.auth import RequiredAuthToken, GetJwtToken, createUser, loginUser

# Initialize blueprint and register it with flask app
AuthApp = Blueprint('Auth App', __name__)


@AuthApp.route('/register', methods=["POST"])
@swag_from('/AuthApp/doc/register.yml')
def registerUser():
    # Get data and json it
    data = request.get_json()
    # Check for null and blank case all data
    if data['firstName'] is None or data['lastName'] is None or data['userName'] is None or data['email'] is None or \
            data['mobile'] is None or data['password'] is None:
        result = ResponseModal(StatusType.fail.value, None, 'Field is empty or null')
        return Response(result, status=400)

    # Check for email is already exist or not
    isEmailExist = User.query.filter_by(email=data['email'], is_delete=False).first()
    if isEmailExist is not None:
        result = ResponseModal(StatusType.fail.value, None, 'Email is already exist')
        return Response(result, status=409)

    # Check for username is already exist or not
    isUserNameExist = User.query.filter_by(username=data['userName'], is_delete=False).first()
    if isUserNameExist is not None:
        result = ResponseModal(StatusType.fail.value, None, 'Username is already exist')
        return Response(result, status=409)

    # Check for mobile is already exist or not
    isMobileExist = User.query.filter_by(mobile=int(data['mobile']), is_delete=False).first()
    if isMobileExist is not None:
        result = ResponseModal(StatusType.fail.value, None, 'Mobile number is already exist')
        return Response(result, status=409)

    # Create user method
    obj = createUser(data)
    if obj is None:
        result = ResponseModal(StatusType.fail.value, None, 'User not created')
        return Response(result, status=400)

    # Serialize data
    schema = UserSchema()
    userData = schema.dumps(obj)
    result = ResponseModal(StatusType.success.value, userData, 'User created successfully')
    return Response(result, status=201)


@AuthApp.route('/login', methods=['POST'])
@swag_from('/AuthApp/doc/login.yml')
def login():
    data = request.get_json()

    # Check for null and blank case all data
    if data['email'] is None or data['password'] is None:
        result = ResponseModal(StatusType.fail.value, None, 'Field is empty or null')
        return Response(result, status=400)

    # User login method
    user = loginUser(data)
    if user['canLogin'] is False:
        result = ResponseModal(StatusType.fail.value, None,
                               'User cannot login check your email and password is correct')
        return Response(result, status=401)

    # Get user object by id
    userObj = User.query.filter_by(id=user['data'], is_delete=False).first()

    tokenTime = {"type": TokenType.accessToken.value, "value": 10}
    access_token = GetJwtToken(userObj, tokenTime)
    tokenTime = {"type": TokenType.refreshToken.value, "value": 1}
    refresh_token = GetJwtToken(userObj, tokenTime)

    tokens = {"access_token": access_token, "refresh_token": refresh_token}
    tokens = json.dumps(tokens)
    result = ResponseModal(StatusType.success.value, tokens, 'User login successfully')
    return Response(result, status=200)


@AuthApp.route('/refresh-token', methods=['GET'])
@swag_from('/AuthApp/doc/refreshToken.yml')
@RequiredAuthToken
def refreshToken(current_user):
    userId = current_user.id
    obj = User.query.filter_by(id=userId).first()
    tokenTime = {"type": TokenType.accessToken.value, "value": 10}
    accessToken = GetJwtToken(obj, tokenTime)
    tokens = json.dumps({"accessToken": accessToken})
    result = ResponseModal(StatusType.success.value, tokens, 'User login successfully')
    return Response(result, status=200)