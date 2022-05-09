from pony.orm import db_session
from core.base import BaseClass, exc_handler
from models.models import *


class DBScheduleController(BaseClass):

    def __init__(self, config):
        BaseClass.__init__(self, config)

    def _add_free_slots(self, _item):
        slots = self._free_at.select(
            lambda a: _item._id == a.schedule_id
        )
        imte = _item.to_dict()
        if slots:
            imte['free_slots'] = [item.to_dict() for item in slots]
        return imte

    '''
    Schedule Methods
    '''
    @db_session
    @exc_handler
    def get_schedules(self, _id):
        schedules = self._schedule.select(
            lambda a: self._user[_id] in a.users
        )
        if schedules:
            response = [self._add_free_slots(item) for item in schedules]
        return dict(schedules=response)

    @db_session
    @exc_handler
    def add_schedule(self, _id, title):
        return self._schedule(title=title, users=self._user[_id])

    @db_session
    @exc_handler
    def delete_schedule(self, _id):
        return self._schedule[_id].delete()

    @db_session
    @exc_handler
    def update_schedule(self, _id, update_data):
        filtered_data = {k: v for k, v in update_data.items() if v is not None}
        self._schedule[_id].set(**filtered_data)
        return self._schedule[_id]
