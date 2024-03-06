# app/api/controllers/user_controller.py

from flask import request
from flask_restx import Resource, Namespace
from app.api.service.user_service import UserService
from app.api.util.error_handler import ErrorHandler
from app.api.exception.not_found_exception import NotFoundException
from app.api.exception.service_exception import ServiceException
from app.api.exception.validation_exception import ValidationException

api = Namespace('users', description='User operations')
user_service = UserService()
error_handler = ErrorHandler(api)
error_handler.register_error_handler()

@api.route('/')
class UserController(Resource):
    @api.doc('create_user')
    def post(self):
        """
        Create a new user
        """
        data = request.json
        try:
            new_user = user_service.create_user(data)
            return new_user, 201
        except ValidationException as e:
            api.abort(400, str(e))

    @api.doc('get_all_users')
    def get(self):
        """
        Get all users
        """
        try:
            users = user_service.get_all_users()
            return users
        except Exception as e:
            api.abort(500, str(e))

    @api.doc('update_user')
    def put(self):
        """
        Update a user by ID
        """
        data = request.json
        user_id = data.get('id')
        if not user_id:
            api.abort(400, "User ID is required")
        try:
            updated_user = user_service.update_user(user_id, data)
            return updated_user
        except NotFoundException as e:
            api.abort(404, str(e))
        except ValidationException as e:
            api.abort(400, str(e))
        except ServiceException as e:
            api.abort(500, str(e))

    @api.doc('delete_user')
    def delete(self):
        """
        Delete a user by ID
        """
        user_id = request.args.get('id')
        if not user_id:
            api.abort(400, "User ID is required")
        try:
            user_service.delete_user(user_id)
            return {'message': 'User deleted'}, 200
        except NotFoundException as e:
            api.abort(404, str(e))
        except ServiceException as e:
            api.abort(500, str(e))
