from pony.orm import db_session
from core.base import BaseClass, exc_handler, update_handler


class DBController(BaseClass):

    def __init__(self):
        BaseClass.__init__(self)

    '''
    Event Types Methods
    '''
    @db_session
    @exc_handler
    def get_event_types_by_user_id(self, _id: int):
        event_types = self._event_type.select(
            lambda e: self._user[_id] in e.users
        )
        response = [item.to_dict() for item in event_types]
        return dict(event_types=response)

    @db_session
    @exc_handler
    def add_types(self, _id: int, type_object: dict):
        # TODO: add duplicate check
        # exist = self.get_event_types_by_user_id(_id)['data']
        return self._event_type(users=self._user[_id], **type_object)

    @db_session
    @exc_handler
    def update_type(self, _id: int, type_object: dict):
        self._event_type[_id].set(**update_handler(type_object))
        return self._event_type[_id]

    @db_session
    @exc_handler
    def delete_type(self, _id):
        self._event_type[_id].delete()
        return True
