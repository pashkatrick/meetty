from fastapi import APIRouter
from core import meeting_controller
from decouple import Config, RepositoryEnv
from models.schemes import Meeting

# TODO: fix that 'config'
env = 'development'
dbg = 'true'
# print(f'env: {env}, debug: {dbg}')
env_config = Config(RepositoryEnv(f'./config/{env}.env'))
dbm = meeting_controller.DBMeetingController(config=env_config)
router = APIRouter()


@router.post('/meeting/{user_id}/add', tags=['events'])
def add_meeting(user_id: int, req: Meeting):
    return dbm.add_meeting(_id=user_id, meeting_object=req.dict())


@router.get('/meeting/{user_id}/all', tags=['events'])
def get_meetings(user_id: int, limit: int = 50, offset: int = 0):
    return dbm.get_meetings(user_id, limit, offset)


@router.get('/meeting/{user_id}/{meeting_id}', tags=['events'])
def get_meeting(user_id: int, meeting_id: int):
    return dbm.get_meeting(_id=meeting_id, user_id=user_id)


@router.put('/meeting/{meeting_id}/update', tags=['events'])
def update_meeting(meeting_id: int, req: Meeting):
    if dbm.update_meeting(meeting_id, req.dict()):
        return dict(status=f'meeting was updated')
    else:
        return dict(status=f'internal error')
