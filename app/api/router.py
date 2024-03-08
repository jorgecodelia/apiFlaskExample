from .util.extensions import api
from .controller.user_controller import UserRouter, UserListRouter, UserEditRouter

class Router():

    def route(app):
        
        # Define routes
        api.add_resource(UserEditRouter, '/v1/user')
        api.add_resource(UserRouter, '/v1/user/<id>')
        api.add_resource(UserListRouter, '/v1/users')