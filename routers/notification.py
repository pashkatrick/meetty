from fastapi import APIRouter
from core import notification_controller
from models.schemes import Notification
from core.base import mssg_response


dbn = notification_controller.DBNotificationController()
router = APIRouter()


@router.post('/notify/email', tags=['notification'])
def send_email(reply_to: str, message: str = 'Hi. that\'s you email from http'):
    return mssg_response(dbn.send_email(reply_to, message))
