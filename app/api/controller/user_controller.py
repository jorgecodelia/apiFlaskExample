from flask import request
from flask_restx import Resource, Namespace
from ..service.user_service import UserService
from ..exception.not_found_exception import NotFoundException
from ..exception.service_exception import ServiceException
from ..exception.validation_exception import ValidationException
from ..util.extensions import api
from ..util.error_handler import ErrorHandler
from ..util.logger_util import LoggerUtil

api = Namespace('users', description='User operations')
user_service = UserService()
error_handler = ErrorHandler(api)
error_handler.register_error_handler()
LOGGER =  LoggerUtil('UserController')

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
        except NotFoundException as e:
            LOGGER.error(type(e), e)
            api.abort(404, str(e))
        except ValidationException as e:
            LOGGER.error(type(e), e)
            api.abort(400, str(e))

    @api.doc('get_user')
    def get(self):
        """
        Get user by id
        """
        user_id = request.args.get('id')
        if not user_id:
            api.abort(400, "User ID is required")
        try:
            user = user_service.get_user(user_id)
            return user
        except NotFoundException as e:
            LOGGER.error(type(e), e)
            api.abort(404, str(e))
        except Exception as e:
            LOGGER.error(type(e), e)
            api.abort(500, str(e))

    @api.doc('get_users')
    def get(self):
        """
        Get all users
        """
        try:
            users = user_service.get_users()
            return users
        except NotFoundException as e:
            LOGGER.error(type(e), e)
            api.abort(404, str(e))
        except Exception as e:
            LOGGER.error(type(e), e)
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
            LOGGER.error(type(e), e)
            api.abort(404, str(e))
        except ValidationException as e:
            LOGGER.error(type(e), e)
            api.abort(400, str(e))
        except ServiceException as e:
            LOGGER.error(type(e), e)
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
            LOGGER.error(type(e), e)
            api.abort(404, str(e))
        except ServiceException as e:
            LOGGER.error(type(e), e)
            api.abort(500, str(e))
