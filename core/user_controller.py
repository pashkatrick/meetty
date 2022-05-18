from pony.orm import db_session
from core.base import BaseClass, exc_handler, update_handler
from models.models import *
from cryptography.fernet import Fernet
from secrets import fernet_key


class DBUserController(BaseClass):

    def __init__(self):
        BaseClass.__init__(self)
        self.fernet = Fernet(fernet_key)

    '''
    User Methods
    '''

    @db_session
    @exc_handler
    def get_user_by_id(self, _id: int, full: bool):
        usr = self._user[_id]
        response = usr.to_dict() if full else f'{usr.name}'
        return dict(user=response)

    @db_session
    @exc_handler
    def get_user_by_name(self, _username: str, full: bool):
        usr = self._user.get(username=_username)
        response = usr.to_dict() if full else f'{usr.name}'
        return dict(user=response)

    @db_session
    @exc_handler
    def get_users(self, limit, offset):
        result = []
        for item in self._user.select()[offset:limit]:
            result.append(item.to_dict())
        return dict(users=result)

    @db_session
    @exc_handler
    def add_user(self, user_object):
        return self._user(**user_object)

    @db_session
    @exc_handler
    def update_user(self, _id, update_data):
        self._user[_id].set(**update_handler(update_data))
        return self._user[_id]

    @db_session
    @exc_handler
    def sign_up(self, _login: str, _pass: str):
        # is_target_user = self.is_user_exist(_login)
        # if not is_target_user:
        return self.add_user(dict(
            username=_login,
            name=_login,
            password=self.fernet.encrypt(_pass.encode())
        )
        )

    @db_session
    @exc_handler
    def sign_in(self, _login: str, _pass: str):
        is_target_user = self.is_user_exist(_login)
        if self.fernet.decrypt(is_target_user.password).decode() == _pass:
            return is_target_user

    @db_session
    @exc_handler
    def is_user_exist(self, _login: str):
        return self._user.select(lambda u: u.username == _login).first()

    @db_session
    @exc_handler
    def upload_avatar(self, _id, file_path):
        self._user[_id].avatar = file_path
        return self._user[_id]

    @db_session
    @exc_handler
    def get_avatar(self, _id):
        return self._user[_id].avatar
