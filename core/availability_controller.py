from datetime import datetime, timedelta
from pony.orm import db_session
from core.base import BaseClass, exc_handler
from core.models import *


class DBTimeController(BaseClass):

    def __init__(self, config):
        BaseClass.__init__(self, config)

    '''
    Free Time Methods
    '''
    @db_session
    @exc_handler
    def get_free_slots_by_user_id(self, _id):
        slots = self._availability.select(
            lambda a: self._user[_id] in a.users
        )
        if slots:
            response = [item.to_dict() for item in slots]
        return dict(data=response)

    @db_session
    @exc_handler
    def add_user_free_slots(self, _id, slots_list):
        exist = []
        for item in self.get_free_slots_by_user_id(_id)['data']:
            del item['_id']
            exist.append(item)
        for slot_object in slots_list:
            if not slot_object in exist:
                self._availability(users=self._user[_id], **slot_object)
                return True
            else:
                return False

    @db_session
    @exc_handler
    def update_free_slots(self, update_id, update_data):
        usr = self._availability[update_id]
        usr.set(**update_data)
        return True

    # def get_slots(self, user_id, event_type_value, date):
    #     # TODO: upgrafe it
    #     days = self.get_days_by_user_id(user_id)
    #     slots = []
    #     for day in days['data']:

    #         ds = datetime.strptime(day['start_time'], '%Y-%d-%mT%H:%M:%S.%fZ')
    #         de = datetime.strptime(day['end_time'], '%Y-%d-%mT%H:%M:%S.%fZ')

    #         while ds < de:
    #             ds += timedelta(minutes=event_type_value)
    #             slots.append(ds.strftime("%H:%M"))
    #     return slots

    '''
    Busy Time Methods
    '''
    @db_session
    @exc_handler
    def get_busy_slots_by_user_id(self, _id):
        slots = self._availability.select(
            lambda a: self._user[_id] in a.users
        )
        if slots:
            response = [item.to_dict() for item in slots]
        return dict(data=response)

    @db_session
    @exc_handler
    def add_user_busy_slots(self, _id, slots_list):
        exist = []
        for item in self.get_free_slots_by_user_id(_id)['data']:
            del item['_id']
            exist.append(item)
        for slot_object in slots_list:
            if not slot_object in exist:
                self._availability(users=self._user[_id], **slot_object)
                return True
            else:
                return False

    @db_session
    @exc_handler
    def update_busy_slots(self, update_id, update_data):
        usr = self._availability[update_id]
        usr.set(**update_data)
        return True