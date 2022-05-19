from pony.orm import db_session
from core.base import BaseClass, exc_handler
from models.models import *
import requests
from secrets import mail_host, api_key, mail_from, attach_name


class DBNotificationController(BaseClass):

    def __init__(self):
        BaseClass.__init__(self)

    '''
    Notification Methods
    '''

    @exc_handler
    def send_email(self, reply_to: str, message: str, subj: str, attach: str):
        payload = {
            'to': [reply_to],
            'from': mail_from,
            'subject': subj,
            'plain_body': message,
            'attachments': [{
                'content_type': 'text/plain',
                'data': attach,
                'name': attach_name
            }]
        }
        return requests.post(f'{mail_host}/api/v1/send/message',
                             json=payload, headers={'X-Server-API-Key': api_key})
