from fastapi import APIRouter
from core import notification_controller
from decouple import Config, RepositoryEnv
from models.schemes import Notification

# TODO: fix that 'config'
env = 'development'
dbg = 'true'
# print(f'env: {env}, debug: {dbg}')
env_config = Config(RepositoryEnv(f'./config/{env}.env'))
dbn = notification_controller.DBNotificationController(config=env_config)
router = APIRouter()


@router.post('/notify/new', tags=['notification'])
def notify_new(req: Notification):
    if dbn.new_event(chat_id=req.dict()['chat_id']):
        return dict(status=f'message was delivered')
    else:
        return dict(status=f'message was not delivered')


@router.post('/notify/approve', tags=['notification'])
def notify_approve(req: Notification):
    if dbn.approve_meeting(chat_id=req.dict()['chat_id']):
        return dict(status=f'message was delivered')
    else:
        return dict(status=f'message was not delivered')


@router.post('/notify/cancel', tags=['notification'])
def notify_cancel(req: Notification):
    if dbn.cancel_meeting(chat_id=req.dict()['chat_id']):
        return dict(status=f'message was delivered')
    else:
        return dict(status=f'message was not delivered')
