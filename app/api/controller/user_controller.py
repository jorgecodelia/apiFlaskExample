from flask import request
from flask_restx import Resource, Namespace, fields
from ..service.user_service import UserService
from ..util.extensions import api
from ..util.logger_util import LoggerUtil
from ..util.constants import Constants
from ..util.validation_util import ValidatorUtil

user_service = UserService()
LOGGER =  LoggerUtil('UserController')

# Define a namespace for the UserController
user_ns = Namespace('users', description='User operations')
api.add_namespace(user_ns)

user_model = user_ns.model('User', {
    'id': fields.Integer(required=None, description='User ID'),
    'name': fields.String(required=True, description='User Name'),
    'email': fields.String(required=True, description='User Email')
})

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
        LOGGER.info("GET ALL USERS")
        users = user_service.get_users()
        return (users, 200)

class UserRouter(Resource):
    @api.doc('get_user')
    @api.param('id', 'User ID', type='integer', required=True)
    @api.response(200, Constants.SUCCESS.value, user_model)
    @api.response(400, Constants.BAD_REQUEST.value)
    @api.response(401, Constants.UNAUTHORIZED.value)
    @api.response(403, Constants.FORBIDDEN.value)
    @api.response(500, Constants.SERVICE_ERROR.value)
    def get(self):
        """
        Get user by id
        """
        user_id = request.args.get('id')
        ValidatorUtil.check_user_id(user_id)
        LOGGER.info("GET USER "+str(user_id))
        user = user_service.get_user(user_id)
        return (user, 200)

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
        ValidatorUtil.check_user_id(user_id)
        LOGGER.info("DELETE USER "+str(user_id))
        user_service.delete_user(user_id)
        return ({'message': 'User deleted'}, 200)

    @api.doc('create_user')
    @api.expect(user_model)
    @api.marshal_with(user_model, code=201)
    @api.response(201, Constants.CREATED.value, user_model)
    @api.response(400, Constants.BAD_REQUEST.value)
    @api.response(401, Constants.UNAUTHORIZED.value)
    @api.response(403, Constants.FORBIDDEN.value)
    @api.response(500, Constants.SERVICE_ERROR.value)
    def post(self):
        """
        Create a new user
        """
        data = request.json
        ValidatorUtil.is_valid_email(data.get('email'))
        LOGGER.info("Create USER "+str(data))
        new_user = user_service.create_user(data)
        return (new_user, 201)

    @api.doc('update_user')
    @api.expect(user_model)
    @api.marshal_with(user_model, code=200)
    @api.response(200, Constants.SUCCESS.value, user_model)
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
        LOGGER.info("UPDATE USER "+str(user_id))
        ValidatorUtil.check_user_id(user_id)
        ValidatorUtil.is_valid_email(data.get('email'))
        updated_user = user_service.update_user(user_id, data)
        return (updated_user,200)