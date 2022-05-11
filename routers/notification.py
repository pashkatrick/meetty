from fastapi import APIRouter
from core import notification_controller
from decouple import Config, RepositoryEnv
from models.schemes import Notification
from core.base import mssg_response

# TODO: fix that 'config'
env = 'development'
dbg = 'true'
# print(f'env: {env}, debug: {dbg}')
env_config = Config(RepositoryEnv(f'./config/{env}.env'))
dbn = notification_controller.DBNotificationController(config=env_config)
router = APIRouter()


@router.post('/notify/new', tags=['notification'])
def notify_new(req: Notification):
    return mssg_response(dbn.new_event(chat_id=req.dict()['chat_id']))


@router.post('/notify/approve', tags=['notification'])
def notify_approve(req: Notification):
    return mssg_response(dbn.approve_meeting(chat_id=req.dict()['chat_id']))


@router.post('/notify/cancel', tags=['notification'])
def notify_cancel(req: Notification):
    return mssg_response(dbn.cancel_meeting(chat_id=req.dict()['chat_id']))
