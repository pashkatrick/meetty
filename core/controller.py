from datetime import datetime, timedelta
# from click import password_option
from pony.orm import db_session
from core.base import BaseClass
import bcrypt
from core.models import *


class DBController(BaseClass):

    def __init__(self, config):
        BaseClass.__init__(self, config)

    '''
    User Methods
    '''

    @db_session
    def get_user_by_id(self, _id: int, full: bool):
        try:
            usr = self._user[_id]
            response = usr.to_dict() if full else f'{usr.name}'
            return dict(data=response)
        except Exception as e:
            return dict(data=f'error: {e}')

    @db_session
    def get_user_by_name(self, _username: str, full: bool):
        try:
            usr = self._user.get(username=_username)
            response = usr.to_dict() if full else f'{usr.name}'
            return dict(data=response)
        except Exception as e:
            return dict(data=f'error: {e}')

    @db_session
    def get_users(self, limit: int = 100, offset: int = 0):
        result = []
        try:
            for item in self._user.select()[offset:limit]:
                result.append(item.to_dict())
            return dict(data=result)
        except Exception as e:
            return dict(data=f'error: {e}')

    @db_session
    def add_user(self, user_object):
        try:
            self._user(**user_object)
            return dict(data='ok')
        except Exception as e:
            return dict(data=f'error: {e}')

    @db_session
    def update_user(self, update_id, update_data):
        usr = self._user[update_id]
        try:
            usr.set(**update_data)
            return dict(data='ok')
        except Exception as e:
            return dict(data=f'error: {e}')

    @db_session
    def sign_up(self, _login: str, _pass: str):
        target_user = self.is_user_exist(_login)
        if target_user:
            return dict(data='user already exist')            
        else:
            # TODO: fix salt
            return self.add_user(dict(username=_login, password=bcrypt.hashpw(_pass, 'super-secret')))

    @db_session
    def sign_in(self, _login: str, _pass: str):
        target_user = self.is_user_exist(_login)
        if not target_user:
            return dict(data='user not found')   
        else:
            # TODO: fix salt
            return bcrypt.checkpw(_pass, bcrypt.hashpw(target_user['passord'], 'super-secret'))
            # return True

    @db_session
    def is_user_exist(self, _login: str):
        try:
            target_user = self._user.select(
                lambda u: u.username == _login
            )
            return target_user
        except:        
            return False

    '''
    Availability Methods
    '''
    @db_session
    def get_days_by_user_id(self, _id):
        try:
            days = self._availability.select(
                lambda a: self._user[_id] in a.users
            )
            if days:
                response = [item.to_dict() for item in days]
            return dict(data=response)
        except Exception as e:
            return dict(data=f'error: {e}')

    @db_session
    def add_days(self, _id, day_object):
        try:
            self._availability(user_id=_id, **day_object)
            return dict(data='ok')
        except Exception as e:
            return dict(data=f'error: {e}')

    @db_session
    def update_days(self, update_id, update_data):
        usr = self._availability[update_id]
        try:
            usr.set(**update_data)
            return dict(data='ok')
        except Exception as e:
            return dict(data=f'error: {e}')

    def get_slots(self, user_id, event_type_value, date):
        # TODO: upgrafe it
        # take a meetings
        # set free status to free slots
        days = self.get_days_by_user_id(user_id)
        slots = []
        for day in days['data']:

            ds = datetime.strptime(day['start_time'], '%Y-%d-%mT%H:%M:%S.%fZ')
            de = datetime.strptime(day['end_time'], '%Y-%d-%mT%H:%M:%S.%fZ')

            while ds < de:
                ds += timedelta(minutes=event_type_value)
                slots.append(ds.strftime("%H:%M"))
        return slots

    '''
    Event Types Methods
    '''
    @db_session
    def get_event_types_by_user_id(self, _id):
        try:
            event_types = self._event_type.select(
                lambda e: self._user[_id] in e.users
            )
            if event_types:
                response = [item.to_dict() for item in event_types]
            return dict(data=response)
        except Exception as e:
            return dict(data=f'error: {e}')

    @db_session
    def add_types(self, _id, type_object):
        try:
            self._event_type(users=self._user[_id], **type_object)
            return dict(data='ok')
        except Exception as e:
            return dict(data=f'error: {e}')

    @db_session
    def update_types(self, update_id, update_data):
        usr = self._event_type[update_id]
        try:
            usr.set(**update_data)
            return dict(data='ok')
        except Exception as e:
            return dict(data=f'error: {e}')

    '''
    Meeting Methods
    '''
    @db_session
    def get_meeting(self, _id: int):
        try:
            mt = self._meeting[_id]
            return dict(data=mt.to_dict())
        except Exception as e:
            return dict(data=f'error: {e}')

    @db_session
    def get_meetings(self, limit: int = 100, offset: int = 0):
        result = []
        try:
            for item in self._meeting.select()[offset:limit]:
                result.append(item.to_dict())
            return dict(data=result)
        except Exception as e:
            return dict(data=f'error: {e}')
