from pony.orm import db_session
from core.base import BaseClass, exc_handler
from core import meeting_controller, notification_controller, availability_controller
from secrets import status_map
from models.schemes import Meeting
import time


class FlowController(BaseClass):

    def __init__(self):
        BaseClass.__init__(self)
        self.dbm = meeting_controller.DBMeetingController()
        self.noty = notification_controller.DBNotificationController()
        self.dba = availability_controller.DBTimeController()

    '''
    Common Flow Methods
    '''

    @db_session
    @exc_handler
    def cancel_meeting(self, _id: int, notify: bool):
        meeting_data = self._meeting[_id]
        self.dbm.update_meeting(
            _id, {'status': status_map['canceled'], 'rejected': True})
        if notify:
            self.dba.delete_busy_slot_by_meeting_id(_id)
            return self.noty.cancel_event_mssg(meeting_data)
        else:
            return self.dba.delete_busy_slot_by_meeting_id(_id)

    @db_session
    @exc_handler
    def create_meeting(self, user_id: int, notify: bool, meeting_object: Meeting):
        meeting_id = self.dbm.add_meeting(user_id, meeting_object.dict())
        busy_object = {
            'time_from': meeting_object.start_time,
            'time_to': meeting_object.end_time,
            'year': meeting_object.year,
            'month': meeting_object.year,
            'day': meeting_object.day,
            'weekday': meeting_object.weekday,
            'meeting_id': meeting_id
        }
        if notify:
            self.dba.add_user_busy_slot(user_id, busy_object)
            return self.noty.apply_event_mssg(meeting_object)
        else:
            return self.dba.add_user_busy_slot(user_id, busy_object)
