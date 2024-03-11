from ..model.user import User
from ..util.logger_util import LoggerUtil

LOGGER =  LoggerUtil('UserRepository')
class UserRepository:
    def __init__(self):
        # This could be a database connection or any other data storage mechanism
        self.users = [
            User(1, 'Alice', 'alice@example.com'),
            User(2, 'Bob', 'bob@example.com')
        ]

    def get_all(self):
        return self.users

    def get_by_id(self, user_id):
        for user in self.users:
            if user.id == user_id:
                return user
        return None

    def create(self, data):
        new_user = User(len(self.users) + 1, data['name'], data['email'])
        self.users.append(new_user)
        return new_user

    def update(self, user_id, data):
        for user in self.users:
            if user.id == user_id:
                user.name = data['name']
                user.email = data['email']
                return user
        return None

    def delete(self, user_id):
        for user in self.users:
            if user.id == user_id:
                return self.users.remove(user)
        return None