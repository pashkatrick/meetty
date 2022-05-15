from email.policy import default
from glob import escape
from pony.orm import db_session
from core.base import BaseClass, exc_handler, update_handler
from models.models import *


class DBScheduleController(BaseClass):

    def __init__(self):
        BaseClass.__init__(self)

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
    def update_schedule(self, _id, user_id, update_data):
        if 'default' in update_data and update_data['default'] == True:
            for schedule in self._schedule.select(lambda r: self._user[user_id] in r.users):
                schedule.set(default=False)
        a = update_handler(update_data)
        return self._schedule[_id].set(**a)
