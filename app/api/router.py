from .util.extensions import api
from .controller.user_controller import UserRouter, UserListRouter

class Router():

    def route():
        
        # Define routes
        api.add_resource(UserRouter, '/v1/user')
        api.add_resource(UserListRouter, '/v1/users')