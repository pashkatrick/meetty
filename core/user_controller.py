from pony.orm import db_session
from core.base import BaseClass, exc_handler
from models.models import *


class DBUserController(BaseClass):

    def __init__(self, config):
        BaseClass.__init__(self, config)

    '''
    User Methods
    '''

    @db_session
    @exc_handler
    def get_user_by_id(self, _id: int, full: bool):
        usr = self._user[_id]
        response = usr.to_dict() if full else f'{usr.name}'
        return dict(data=response)

    @db_session
    @exc_handler
    def get_user_by_name(self, _username: str, full: bool):
        usr = self._user.get(username=_username)
        response = usr.to_dict() if full else f'{usr.name}'
        return dict(data=response)

    @db_session
    @exc_handler
    def get_users(self, limit, offset):
        result = []
        for item in self._user.select()[offset:limit]:
            result.append(item.to_dict())
        return dict(data=result)

    @db_session
    @exc_handler
    def add_user(self, user_object):
        return self._user(**user_object)

    @db_session
    @exc_handler
    def update_user(self, update_id, update_data):
        usr = self._user[update_id]
        return usr.set(**update_data)

    @db_session
    @exc_handler
    def sign_up(self, _login: str, _pass: str):
        # is_target_user = self.is_user_exist(_login)
        # if not is_target_user:
        return self.add_user(dict(username=_login, name=_login, password=_pass))

    @db_session
    @exc_handler
    def sign_in(self, _login: str, _pass: str):
        is_target_user = self.is_user_exist(_login)
        # a = bcrypt.checkpw(_pass.encode('utf-8'), bcrypt.hashpw(target_user.password.encode('utf-8'), b'$2b$12$xdZ1i4SXX6OwCx2WiRJEme'))
        return is_target_user

    @db_session
    @exc_handler
    def is_user_exist(self, _login: str):
        return self._user.select(lambda u: u.username == _login).first()