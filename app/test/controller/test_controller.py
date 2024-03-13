# app/test/controller/test_controller.py

from unittest.mock import patch
from ...api.controller.user_controller import UserRouter, UserListRouter
from ...api.service.user_service import UserService
from ...api.exception.service_exception import ServiceException

def test_create_user_ok():
    with patch.object(UserService, 'create_user', return_value={'id': 1, 'name': 'John Doe', 'email': 'john@example.com'}):
        response = UserRouter().post()
        assert response == ({'id': 1, 'name': 'John Doe', 'email': 'john@example.com'}, 201)
        
def test_create_user_service_error():
    with patch.object(UserService, 'create_user', side_effect=ServiceException("Service error")):
        response = UserRouter().post()
        assert response == ({"message": "Service error"}, 500)

def test_create_user_generic_exception():
    with patch.object(UserService, 'create_user', side_effect=Exception("Service Unavailable")):
        response = UserRouter().post()
        assert response == ({"message": "Service Unavailable"}, 503)
