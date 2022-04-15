from pony.orm import db_session
from core.base import BaseClass, exc_handler
from models.models import *


class DBNotificationController(BaseClass):

    def __init__(self, config):
        BaseClass.__init__(self, config)

    '''
    Notification Methods
    '''

    @db_session
    @exc_handler
    def cancel_meeting(self, meeting_object: dict):
        pass

    @db_session
    @exc_handler
    def approve_meeting(self, meeting_object: dict):
        pass

    # @db_session
    # @exc_handler
    # def get_meeting(self, _id: int):
    #     mt = self._meeting[_id]
    #     return dict(meeting=mt.to_dict())

    # @db_session
    # @exc_handler
    # def get_meetings(self, limit, offset):
    #     result = []
    #     for item in self._meeting.select()[offset:limit]:
    #         result.append(item.to_dict())
    #     return dict(meetings=result)

    # @db_session
    # @exc_handler
    # def add_meeding(self, meeting_object: dict):
    #     return self._user(**meeting_object)
