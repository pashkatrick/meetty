from datetime import datetime, timedelta
from pony.orm import db_session
from core.base import BaseClass
from core.models import *


class DBController(BaseClass):

    def __init__(self, config):
        BaseClass.__init__(self, config)


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
            print(f'error: {e}')
            return False

    @db_session
    def add_days(self, _id, day_object):
        try:
            self._availability(user_id=_id, **day_object)
            return True
        except Exception as e:
            print(f'error: {e}')
            return False

    @db_session
    def update_days(self, update_id, update_data):
        usr = self._availability[update_id]
        try:
            usr.set(**update_data)
            return True
        except Exception as e:
            print(f'error: {e}')
            return False

    def get_slots(self, user_id, event_type_value, date):
        # TODO: upgrafe it
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
            print(f'error: {e}')
            return False

    @db_session
    def add_types(self, _id, type_object):
        try:
            self._event_type(users=self._user[_id], **type_object)
            return True
        except Exception as e:
            print(f'error: {e}')
            return False

    @db_session
    def update_types(self, update_id, update_data):
        usr = self._event_type[update_id]
        try:
            usr.set(**update_data)
            return True
        except Exception as e:
            print(f'error: {e}')
            return False
