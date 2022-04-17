from pony.orm import db_session
from core.base import BaseClass, exc_handler
from models.models import *
import requests


class DBNotificationController(BaseClass):

    def __init__(self, config):
        BaseClass.__init__(self, config)

    host = 'https://n8n.pshktrck.ru/webhook/36e771a5-162c-4f96-8d23-bee10432dfb9'
    payload_new = {
        'telegram_chat_id': '',
        'text': 'Hi there!\nyou have new event. Check, please!'
    }

    payload_approve = {
        'telegram_chat_id': '',
        'text': 'Hi there!\nyour meeting was approved by other side. Welcome!'
    }

    payload_cancel = {
        'telegram_chat_id': '',
        'text': 'Hi there!\nyour meeting was canceled by other side. Sorry!'
    }

    '''
    Notification Methods
    '''
    @db_session
    @exc_handler
    def new_event(self, chat_id):
        body = self.payload_new
        body['telegram_chat_id'] = chat_id
        return requests.post(self.host, json=body)

    @db_session
    @exc_handler
    def cancel_meeting(self, chat_id):
        body = self.payload_cancel
        body['telegram_chat_id'] = chat_id
        return requests.post(self.host, json=body)

    @db_session
    @exc_handler
    def approve_meeting(self, chat_id):
        body = self.payload_approve
        body['telegram_chat_id'] = chat_id
        return requests.post(self.host, json=body)
