from fastapi import APIRouter
from core import schedule_controller
from decouple import Config, RepositoryEnv
from models.schemes import Schedule

# TODO: fix that 'config'
env = 'development'
dbg = 'true'
# print(f'env: {env}, debug: {dbg}')
env_config = Config(RepositoryEnv(f'./config/{env}.env'))
dbs = schedule_controller.DBScheduleController(config=env_config)
router = APIRouter()


@router.get('/user/{user_id}/schedules', tags=['schedule'])
def get_schedules(user_id: int):
    return dbs.get_schedules(_id=user_id)


@router.post('/user/{user_id}/schedules', tags=['schedule'])
def add_schedule(user_id: int, req: Schedule):
    if dbs.add_schedule(_id=user_id, title=req.dict()['title']):
        return dict(status=f'schedule was added')
    else:
        return dict(status=f'duplicate or internal error')


@router.delete('/schedule/{schedule_id}/delete', tags=['schedule'])
def delete_schedule(schedule_id: int):
    if dbs.delete_schedule(_id=schedule_id):
        return dict(status=f'schedule was deleted')
    else:
        return dict(status=f'internal error')


@router.put('/schedule/{schedule_id}/update', tags=['schedule'])
def update_schedule(schedule_id: int, req: Schedule):
    if dbs.update_schedule(schedule_id, req.dict()):
        return dict(status=f'schedule was updated')
    else:
        return dict(status=f'internal error')
