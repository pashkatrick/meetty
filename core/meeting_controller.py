from pony.orm import db_session
from core.base import BaseClass, exc_handler, update_handler
import uuid


class DBMeetingController(BaseClass):

    def __init__(self):
        BaseClass.__init__(self)

    '''
    Meeting Methods
    '''

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
    def get_meetings(self, _id: int, limit: int, offset: int, status: int):
        if status:
            meetings = self._meeting.select(
                lambda m: self._user[_id]._id == m.user_id and m.status == status
            )[offset:limit]
        else:
            meetings = self._meeting.select(
                lambda m: self._user[_id]._id == m.user_id
            )[offset:limit]
        response = [item.to_dict() for item in meetings]
        return dict(meetings=response)

    @db_session
    @exc_handler
    def add_meeting(self, user_id: int, meeting_object: dict):
        meeting_object['uuid'] = str(uuid.uuid4())
        return self._meeting(user_id=self._user[user_id]._id, **meeting_object)

    @db_session
    @exc_handler
    def update_meeting(self, _id: int, update_data: dict):
        self._meeting[_id].set(**update_handler(update_data))
        return self._meeting[_id]
