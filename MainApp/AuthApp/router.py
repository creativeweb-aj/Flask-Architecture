from flask import Response
from flask_restx import Resource
from MainApp.AuthApp.app import AuthApi
from MainApp.AppSettings.response import StatusType, ResponseModal


# Auth App Api

@AuthApi.route('/login', methods=['GET'])
class Index(Resource):
    def get(self):
        result = ResponseModal(
            StatusType.success.value,
            data='This is your first test api called.',
            message='Data sent successfully!'
        )
        return Response(result, status=200)
