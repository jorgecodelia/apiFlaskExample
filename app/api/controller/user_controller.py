from flask import request
from flask_restx import Resource, Namespace
from ..service.user_service import UserService
from ..util.extensions import api
from ..util.error_handler import ErrorHandler
from ..util.logger_util import LoggerUtil
from ..util.constants import Constants

api = Namespace('users', description='User operations')
user_service = UserService()
handler = ErrorHandler()
LOGGER =  LoggerUtil('UserController')

class UserListRouter(Resource):
    @api.doc('get_users')
    @api.response(200, Constants.SUCCESS.value)
    @api.response(400, Constants.BAD_REQUEST.value)
    @api.response(401, Constants.UNAUTHORIZED.value)
    @api.response(403, Constants.FORBIDDEN.value)
    @api.response(500, Constants.SERVICE_ERROR.value)
    def get(self):
        """
        Get all users
        """
        try:
            users = user_service.get_users()
            return (users, 200)
        except Exception as e:
            LOGGER.error(type(e), e)
            handler.handle_exception(e)

class UserRouter(Resource):
    @api.doc('get_user')
    @api.param('id', 'User ID', type='integer', required=True)
    @api.response(200, Constants.SUCCESS.value)
    @api.response(400, Constants.BAD_REQUEST.value)
    @api.response(401, Constants.UNAUTHORIZED.value)
    @api.response(403, Constants.FORBIDDEN.value)
    @api.response(500, Constants.SERVICE_ERROR.value)
    def get(self):
        """
        Get user by id
        """
        user_id = request.args.get('id')
        if not user_id:
            api.abort(400, "User ID is required")
        try:
            user = user_service.get_user(user_id)
            return (user, 200)
        except Exception as e:
            LOGGER.error(type(e), e)
            handler.handle_exception(e)

    @api.doc('delete_user')
    @api.param('id', 'User ID', type='integer', required=True)
    @api.response(200, Constants.SUCCESS.value)
    @api.response(400, Constants.BAD_REQUEST.value)
    @api.response(401, Constants.UNAUTHORIZED.value)
    @api.response(403, Constants.FORBIDDEN.value)
    @api.response(500, Constants.SERVICE_ERROR.value)
    def delete(self):
        """
        Delete a user by ID
        """
        user_id = request.args.get('id')
        if not user_id:
            api.abort(400, "User ID is required")
        try:
            user_service.delete_user(user_id)
            return ({'message': 'User deleted'}, 200)
        except Exception as e:
            LOGGER.error(type(e), e)
            handler.handle_exception(e)


class UserEditRouter(Resource):
    @api.doc('create_user')
    @api.response(201, Constants.CREATED.value)
    @api.response(400, Constants.BAD_REQUEST.value)
    @api.response(401, Constants.UNAUTHORIZED.value)
    @api.response(403, Constants.FORBIDDEN.value)
    @api.response(500, Constants.SERVICE_ERROR.value)
    def post(self):
        """
        Create a new user
        """
        data = request.json
        user_id = data.get('id')
        if not user_id:
            api.abort(400, "User ID is required")
        try:
            new_user = user_service.create_user(data)
            return (new_user, 201)
        except Exception as e:
            LOGGER.error(type(e), e)
            handler.handle_exception(e)

    @api.doc('update_user')
    @api.response(200, Constants.SUCCESS.value)
    @api.response(400, Constants.BAD_REQUEST.value)
    @api.response(401, Constants.UNAUTHORIZED.value)
    @api.response(403, Constants.FORBIDDEN.value)
    @api.response(500, Constants.SERVICE_ERROR.value)
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
            return (updated_user,200)
        except Exception as e:
            LOGGER.error(type(e), e)
            handler.handle_exception(e)