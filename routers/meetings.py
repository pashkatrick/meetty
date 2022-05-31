from fastapi import APIRouter, Query
from core import meeting_controller, flow_controller
from models.schemes import Meeting
from core.base import condition_response
from secrets import status_map

dbm = meeting_controller.DBMeetingController()
flow = flow_controller.FlowController()
router = APIRouter()


@router.post('/meeting/{user_id}/create', tags=['events'])
def add_meeting(user_id: int, req: Meeting):
    return flow.create_meeting(user_id, meeting_object=req.dict())


@router.get('/meeting/{user_id}/all', tags=['events'])
def get_meetings(user_id: int, limit: int = 50, offset: int = 0, status: str = Query('status', enum=['upcoming', 'past', 'canceled'])):
    return dbm.get_meetings(user_id, limit, offset, status_map[status])


@router.get('/meeting/{user_id}/{meeting_id}', tags=['events'])
def get_meeting(user_id: int, meeting_id: int):
    return dbm.get_meeting(_id=meeting_id, user_id=user_id)


@router.put('/meeting/{meeting_id}/update', tags=['events'])
def update_meeting(meeting_id: int, req: Meeting):
    return condition_response(dbm.update_meeting(meeting_id, req.dict()))


# @router.post('/meeting/{user_id}/create', tags=['events'])
# def create_meeting(user_id: int, req: Meeting):
#     return flow.create_meeting(user_id, meeting_object=req.dict())


@router.post('/meeting/{meeting_id}/cancel', tags=['events'])
def update_meeting(meeting_id: int):
    return condition_response(flow.cancel_meeting(meeting_id))
