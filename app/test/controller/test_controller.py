# app/test/controller/test_controller.py

from unittest.mock import patch
from ...api.controller.user_controller import UserController
from ...api.service.user_service import UserService
from ...api.exception.service_exception import ServiceException
from ...api.exception.validation_exception import ValidationException

def test_create_user_ok():
    with patch.object(UserService, 'create_user', return_value={'id': 1, 'name': 'John Doe', 'email': 'john@example.com'}):
        response = UserController().post()
        assert response == ({'id': 1, 'name': 'John Doe', 'email': 'john@example.com'}, 201)

def test_create_user_validation_error():
    with patch.object(UserService, 'create_user', side_effect=ValidationException("Validation error")):
        response = UserController().post()
        assert response == ({"message": "Validation error"}, 400)
        
def test_create_user_service_error():
    with patch.object(UserService, 'create_user', side_effect=ServiceException("Service error")):
        response = UserController().post()
        assert response == ({"message": "Service error"}, 500)

def test_create_user_generic_exception():
    with patch.object(UserService, 'create_user', side_effect=Exception("Service Unavailable")):
        response = UserController().post()
        assert response == ({"message": "Service Unavailable"}, 503)
