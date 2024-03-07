# app/test/repository/test_repository.py

import unittest
from ...api.repository.user_repository import UserRepository

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.user_repository = UserRepository()

    def test_get_all_users(self):
        users = self.user_repository.get_all()
        self.assertTrue(len(users) > 0)
