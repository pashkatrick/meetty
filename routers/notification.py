from fastapi import APIRouter, Depends
from core import notification_controller
from core.base import mssg_response
from fastapi.security import HTTPBearer
from fastapi_jwt_auth import AuthJWT


dbn = notification_controller.DBNotificationController()
router = APIRouter()

# need for docs auth button
token_auth_scheme = HTTPBearer()


@router.post('/notify/email', tags=['notification'])
def send_email(
        reply_to: str,
        attach: str,
        subject: str = 'Event between <user> and <user>',
        message: str = '<user> requested you for meeting, details:',
        Authorize: AuthJWT = Depends(), token=Depends(token_auth_scheme)
):
    Authorize.jwt_required()
    return mssg_response(dbn.send_email(reply_to, subject, message, attach))
