# app/test/conftest.py

import os
import pytest
import shutil
from app.api.repository.user_repository import UserRepository
from app.api.service.user_service import UserService
from app.api.controller.user_controller import UserRouter, UserListRouter
from unittest.mock import MagicMock

@pytest.fixture
def user_repository():
    # Create an instance of UserRepository for each test function
    return UserRepository()

@pytest.fixture
def user_service(user_repository):
    # Create an instance of UserService for each test function
    return UserService(user_repository)

@pytest.fixture
def user_controller(user_service):
    # Create an instance of UserList and User controllers for each test function
    return UserRouter(user_service)

@pytest.fixture
def user_controller(user_service):
    # Create an instance of UserList and User controllers for each test function
    return UserListRouter(user_service)

class CleanUpAfterTest:
    @staticmethod
    def clean_pyc(directory):
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith('.pyc'):
                    os.remove(os.path.join(root, file))
            for dir in dirs:
                if dir == '__pycache__':
                    shutil.rmtree(os.path.join(root, dir))

if __name__ == "__main__":
    CleanUpAfterTest.clean_pyc('.')
