import imp
from core.base import BaseClass, exc_handler
import requests
from secrets import mail_host, api_key, mail_from, attach_name, cancel_message, apply_message
from pprint import pprint
from models.schemes import Meeting


class DBNotificationController(BaseClass):

    def __init__(self):
        BaseClass.__init__(self)

    '''
    Notification Methods
    '''

    @exc_handler
    def send_email(self, reply_to: str, message: str, subj: str, attach: str = None):
        payload = {
            'to': [reply_to],
            'from': mail_from,
            'subject': subj,
            'plain_body': message
        }
        if attach is not None:
            payload['attachments'] = [{
                'content_type': 'text/plain',
                'data': attach,
                'name': attach_name
            }]
        return requests.post(f'{mail_host}/api/v1/send/message',
                             json=payload, headers={'X-Server-API-Key': api_key})

    @exc_handler
    def cancel_event_mssg(self, event_data: Meeting):
        return self.send_email(
            reply_to=event_data.recepient_email,
            message=f"Cancel Event: {event_data.title}",
            subj=f"Cancel Event: {event_data.title}",
        )

    @exc_handler
    def apply_event_mssg(self, event_data: Meeting):
        return self.send_email(
            reply_to=event_data.recepient_email,
            message=f'Apply Event: {event_data.title}',
            subj=f'Apply Event: {event_data.title}'
        )
