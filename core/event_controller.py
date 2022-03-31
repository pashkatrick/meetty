from pony.orm import db_session
from core.base import BaseClass, exc_handler
from models.models import *


class DBController(BaseClass):

    def __init__(self, config):
        BaseClass.__init__(self, config)

    '''
    Event Types Methods
    '''
    @db_session
    @exc_handler
    def get_event_types_by_user_id(self, _id):
        event_types = self._event_type.select(
            lambda e: self._user[_id] in e.users
        )
        if event_types:
            response = [item.to_dict() for item in event_types]
        return dict(data=response)

    @db_session
    @exc_handler
    def add_types(self, _id, type_object: dict):
        # TODO: add duplicate check
        # exist = self.get_event_types_by_user_id(_id)['data']
        return self._event_type(users=self._user[_id], **type_object)

    @db_session
    @exc_handler
    def update_types(self, update_id, update_data):
        usr = self._event_type[update_id]
        usr.set(**update_data)
        return True
