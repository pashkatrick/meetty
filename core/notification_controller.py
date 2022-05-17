from pony.orm import db_session
from core.base import BaseClass, exc_handler
from models.models import *
import requests


class DBNotificationController(BaseClass):

    def __init__(self):
        BaseClass.__init__(self)

    '''
    Notification Methods
    '''

    @exc_handler
    def send_email(self, reply_to: str, message: str):
        payload = {
            "to": [reply_to],
            "from": "hi@meetty.me",
            "subject": "Meetty Event",
            "plain_body": message
        }
        return requests.post('http://inbox.meetty.me:5000/api/v1/send/message',
                             json=payload, headers={'X-Server-API-Key': 'CArhxXCiRqUPKjZqOKC5cKcL'})
