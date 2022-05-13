from fastapi import APIRouter
from core import schedule_controller
from models.schemes import Schedule
from core.base import condition_response

dbs = schedule_controller.DBScheduleController()
router = APIRouter()


@router.get('/user/{user_id}/schedules', tags=['schedule'])
def get_schedules(user_id: int):
    return dbs.get_schedules(_id=user_id)


@router.post('/user/{user_id}/schedules', tags=['schedule'])
def add_schedule(user_id: int, req: Schedule):
    return condition_response(dbs.add_schedule(_id=user_id, title=req.dict()['title']))


@router.delete('/schedule/{schedule_id}/delete', tags=['schedule'])
def delete_schedule(schedule_id: int):
    return condition_response(dbs.delete_schedule(_id=schedule_id))


@router.put('/schedule/{schedule_id}/update', tags=['schedule'])
def update_schedule(schedule_id: int, req: Schedule):
    return condition_response(dbs.update_schedule(schedule_id, req.dict()))
