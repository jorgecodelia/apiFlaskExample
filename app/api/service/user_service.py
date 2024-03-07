from ..repository.user_repository import UserRepository

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def get_users(self):
        return self.user_repository.get_all()

    def get_user(self, user_id):
        return self.user_repository.get_by_id(user_id)

    def create_user(self, data):
        return self.user_repository.create(data)

    def update_user(self, user_id, data):
        return self.user_repository.update(user_id, data)

    def delete_user(self, user_id):
        return self.user_repository.delete(user_id)