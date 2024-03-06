# app/test/controller/test_controller.py

from unittest.mock import patch
from app.api.controller.user_controller import UserController
from app.api.service.user_service import UserService
from app.api.common.exception import NotFoundException, ValidationError, ServiceException
import json

def test_create_user_ok():
    with patch.object(UserService, 'create_user', return_value={'id': 1, 'name': 'John Doe', 'email': 'john@example.com'}):
        response = UserController().post()
        assert response == ({'id': 1, 'name': 'John Doe', 'email': 'john@example.com'}, 201)

def test_create_user_validation_error():
    with patch.object(UserService, 'create_user', side_effect=ValidationError("Validation error")):
        response = UserController().post()
        assert response == ({"message": "Validation error"}, 400)

def test_create_user_service_exception():
    with patch.object(UserService, 'create_user', side_effect=Exception("Service exception")):
        response = UserController().post()
        assert response == ({"message": "Service exception"}, 500)
