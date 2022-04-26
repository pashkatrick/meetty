from os import stat, stat_result
from pony.orm import db_session
from core.base import BaseClass, exc_handler
from models.models import *


class DBMeetingController(BaseClass):

    def __init__(self, config):
        BaseClass.__init__(self, config)

    '''
    Meeting Methods
    '''

    status_map = {
        'upcoming': 1,
        'past': 2,
        'canceled': 3
    }

    @db_session
    @exc_handler
    def get_meeting(self, _id: int, user_id: int):
        meeting = list(self._meeting.select(
            lambda m: self._user[user_id]._id == m.user_id and m._id == _id
        ))[0]
        if meeting:
            return dict(meeting=meeting.to_dict())

    @db_session
    @exc_handler
    def get_meetings(self, _id, limit, offset, status):
        status_value = self.status_map[status]
        if status_value:
            meetings = self._meeting.select(
                lambda m: self._user[_id]._id == m.user_id and m.status == status_value
            )[offset:limit]
        else: 
            meetings = self._meeting.select(
                lambda m: self._user[_id]._id == m.user_id
            )[offset:limit]            
        if meetings:
            response = [item.to_dict() for item in meetings]
        return dict(meetings=response)

    @db_session
    @exc_handler
    def add_meeting(self, _id: int, meeting_object: dict):
        return self._meeting(user_id=self._user[_id]._id, **meeting_object)
