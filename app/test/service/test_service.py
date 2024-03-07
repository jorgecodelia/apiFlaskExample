# app/test/test_service.py

import unittest
from ...api.service.user_service import UserService

class TestUserService(unittest.TestCase):
    def setUp(self):
        self.user_service = UserService()

    def test_get_all_users(self):
        users = self.user_service.get_users()
        self.assertTrue(len(users) > 0)

