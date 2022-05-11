from fastapi import APIRouter
from core import availability_controller
from decouple import Config, RepositoryEnv
from models.schemes import Slots, SlotsList
from core.base import condition_response

# TODO: fix that 'config'
env = 'development'
dbg = 'true'
# print(f'env: {env}, debug: {dbg}')
env_config = Config(RepositoryEnv(f'./config/{env}.env'))
dba = availability_controller.DBTimeController(config=env_config)
router = APIRouter()


@router.get('/user/{user_id}/free', tags=['time slots'])
def get_free_slots_by_user_id(user_id: int):
    return dba.get_free_slots_by_user_id(_id=user_id)


@router.post('/user/{user_id}/free/add', tags=['time slots'])
def add_user_free_slots(user_id: int, req: SlotsList):
    return condition_response(dba.add_user_free_slots(_id=user_id, slots_list=req.dict()['slots']))


@router.put('/slot/{slot_id}/update', tags=['time slots'])
def update_free_slot(slot_id: int, req: Slots):
    return condition_response(dba.update_free_slot(slot_id, req.dict()))


@router.delete('/slot/{slot_id}/delete', tags=['time slots'])
def update_free_slot(slot_id: int):
    return condition_response(dba.delete_time_slot(slot_id))


@router.get('/user/{user_id}/busy', tags=['time slots'])
def get_busy_slots_by_user_id(user_id: int):
    return dba.get_busy_slots_by_user_id(_id=user_id)


@router.post('/user/{user_id}/busy/add', tags=['time slots'])
def add_user_busy_slots(user_id: int, req: SlotsList):
    return condition_response(dba.add_user_busy_slots(_id=user_id, slots_list=req.dict()['slots']))
