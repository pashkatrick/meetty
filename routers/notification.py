from fastapi import APIRouter
from core import notification_controller
from models.schemes import Notification
from core.base import mssg_response


dbn = notification_controller.DBNotificationController()
router = APIRouter()


@router.post('/notify/email', tags=['notification'])
def send_email(
        reply_to: str, attach: str | None, subject: str = 'Event between <user> and <user>',
        message: str = '<user> requested you for meeting, details:'):
    return mssg_response(dbn.send_email(reply_to, subject, message, attach))
