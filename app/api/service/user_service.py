from ..repository.user_repository import UserRepository
from ..exception.not_found_exception import NotFoundException
from ..util.logger_util import LoggerUtil
from ..util.error_handler import ErrorHandler

LOGGER =  LoggerUtil('UserService')
HANDLER = ErrorHandler()

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def get_users(self):
        users = self.user_repository.get_all()
        serialized_users = [user.to_dict() for user in users]
        return serialized_users

    def get_user(self, user_id):
        user = self.user_repository.get_by_id(int(user_id))
        if not user:
            e = NotFoundException("User not found!")
            LOGGER.error(type(e), e.description)
            HANDLER.handle_exception(e)
        else:
            return user.to_dict()

    def create_user(self, data):
        new_user = self.user_repository.create(data)
        return new_user.to_dict()

    def update_user(self, user_id, data):
        self.get_user(user_id)
        user = self.user_repository.update(user_id, data)
        return user.to_dict()

    def delete_user(self, user_id):
        self.get_user(user_id)
        return self.user_repository.delete(int(user_id))
    