from pony.orm import db_session
from core.base import BaseClass, exc_handler
from models.models import *


class DBMeetingController(BaseClass):

    def __init__(self, config):
        BaseClass.__init__(self, config)

    '''
    Meeting Methods
    '''

    @db_session
    @exc_handler
    def get_meeting(self, _id: int):
        mt = self._meeting[_id]
        return dict(data=mt.to_dict())

    @db_session
    @exc_handler
    def get_meetings(self, limit, offset):
        result = []
        for item in self._meeting.select()[offset:limit]:
            result.append(item.to_dict())
        return dict(data=result)

    @db_session
    @exc_handler
    def add_meeding(self, meeting_object: dict):
        return self._user(**meeting_object)
