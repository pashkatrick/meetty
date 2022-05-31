from pony.orm import db_session
from core.base import BaseClass, exc_handler
from core import meeting_controller, notification_controller, availability_controller
from secrets import status_map


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
    def cancel_meeting(self, _id: int):
        meeting_data = self._meeting[_id]
        self.dbm.update_meeting(_id, {'status': status_map['canceled']})
        self.noty.cancel_event_mssg(meeting_data.json())

    @db_session
    @exc_handler
    def create_meeting(self, user_id: int, meeting_object: dict):
        self.dbm.add_meeting(user_id, meeting_object)
        self.noty.apply_event_mssg(meeting_object)
