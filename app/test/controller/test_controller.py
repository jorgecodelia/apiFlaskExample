# app/test/controller/test_controller.py

import json
import unittest
from app.api.controller.user_controller import UserRouter, UserListRouter
from app.api.service.user_service import UserService
from app.api.exception.service_exception import ServiceException

class TestUserController(unittest.TestCase):
    def setUp(self):
        self.user_router = UserRouter()
        self.user_list_router = UserListRouter()
        self.user_service = UserService()

    def test_get_all_users(self):
        users = self.user_list_router.get()
        self.assertTrue(len(users) > 0)