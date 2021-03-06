from pony.orm import db_session
from core.base import BaseClass, exc_handler, update_handler


class DBTimeController(BaseClass):

    def __init__(self):
        BaseClass.__init__(self)

    '''
    Free Time Methods
    '''
    @db_session
    @exc_handler
    def get_free_slots_by_user_id(self, _id: int):
        slots = self._free_at.select(
            lambda f: self._user[_id] in f.users
        )
        response = [item.to_dict() for item in slots]
        return dict(free_slots=response)

    @db_session
    @exc_handler
    def add_user_free_slots(self, _id: int, slots_list: list):
        # exist = []
        # for item in self.get_free_slots_by_user_id(_id)['free_slots']:
        #     del item['_id']
        #     # TODO: only one add, but second miss in list
        #     exist.append(item)
        for slot_object in slots_list:
            # if not slot_object in exist:
            self._free_at(users=self._user[_id], **slot_object)
        return True

    @db_session
    @exc_handler
    def update_free_slot(self, _id: int, update_data: dict):
        self._free_at[_id].set(**update_handler(update_data))
        return self._free_at[_id]

    @db_session
    @exc_handler
    def delete_free_slot(self, _id):
        self._free_at[_id].delete()
        return True

    '''
    Busy Time Methods
    '''
    @db_session
    @exc_handler
    def get_busy_slots_by_user_id(self, _id: int):
        slots = self._busy_at.select(
            lambda a: self._user[_id] in a.users
        )
        response = [item.to_dict() for item in slots]
        return dict(busy_slots=response)

    @db_session
    @exc_handler
    def add_user_busy_slots(self, user_id: int, slots_list: list):
        # exist = []
        # for item in self.get_busy_slots_by_user_id(_id)['busy_slots']:
        #     del item['_id']
        #     # TODO: only one add, but second miss in list
        #     exist.append(item)
        for slot_object in slots_list:
            # if not slot_object in exist:
            self._busy_at(users=self._user[user_id], **slot_object)
        return True

    @db_session
    @exc_handler
    def add_user_busy_slot(self, user_id: int, slot_object: dict):
        self._busy_at(users=self._user[user_id], **slot_object)
        return True

    @db_session
    @exc_handler
    def update_busy_slot(self, _id: int, update_data: dict):
        self._busy_at[_id].set(**update_handler(update_data))
        return self._busy_at[_id]

    @db_session
    @exc_handler
    def delete_busy_slot(self, _id):
        self._busy_at[_id].delete()
        return True

    @db_session
    @exc_handler
    def delete_busy_slot_by_meeting_id(self, meeting_id):
        self._busy_at.select(lambda b: b.meeting_id == meeting_id).delete()
        return True
