from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from decouple import Config, RepositoryEnv
from core import event_controller, user_controller, meeting_controller, availability_controller, notification_controller, schedule_controller
from fastapi import FastAPI, Depends
from fastapi.security import HTTPBearer
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn
from models.schemes import *

app = FastAPI()

# TODO: config

origins = [
    'http://109.107.176.29',
    'http://109.107.176.29:5000',
    'http://localhost',
    'http://localhost:5000',
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# TODO: fix that 'config'
env = 'development'
dbg = 'true'
print(f'env: {env}, debug: {dbg}')
env_config = Config(RepositoryEnv(f'./config/{env}.env'))
dbe = event_controller.DBController(config=env_config)
dbu = user_controller.DBUserController(config=env_config)
dbm = meeting_controller.DBMeetingController(config=env_config)
dba = availability_controller.DBTimeController(config=env_config)
dbn = notification_controller.DBNotificationController(config=env_config)
dbs = schedule_controller.DBScheduleController(config=env_config)

# need for docs auth button
token_auth_scheme = HTTPBearer()


@AuthJWT.load_config
def get_config():
    return Settings()


@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request, exc: AuthJWTException):
    return JSONResponse(status_code=exc.status_code, content={'detail': exc.message})


@app.get('/ready')
def ready(Authorize: AuthJWT = Depends(), token=Depends(token_auth_scheme)):
    Authorize.jwt_required()
    current_user = Authorize.get_jwt_subject()
    return dict(status=f'ok, {current_user}')


@app.get('/', tags=['index'])
def index():
    return dict(data='Welcome to Calendario')


@app.post('/auth/signup', tags=['auth'])
def registration(req: Auth):
    user_login = req.login
    user_pass = req.password
    if dbu.sign_up(user_login, user_pass):
        return dict(status=f'user {user_login} was registered')
    else:
        return dict(data=f'user {user_login} already exist')


@app.post('/auth/signin', tags=['auth'])
def login(req: Auth, Authorize: AuthJWT = Depends()):
    user_login = req.login
    user_pass = req.password
    if dbu.sign_in(user_login, user_pass):
        access_token = Authorize.create_access_token(subject=user_login)
        return dict(token=access_token)
    else:
        return dict(data='user doesn\'t exist')


@app.get('/users', tags=['users'])
def get_users(limit: int = 50, offset: int = 0):
    return dbu.get_users(limit, offset)


@app.get('/{username}', tags=['users'])
def get_user_by_name(username: str, full: bool = False):
    return dbu.get_user_by_name(_username=username, full=full)


@app.get('/user/{username}')
def get_user_by_name(username: str, full: bool = False):
    return dbu.get_user_by_name(_username=username, full=full)


@app.get('/user/id/{user_id}', tags=['users'])
def get_user_by_id(user_id: int, full: bool = False):
    return dbu.get_user_by_id(_id=user_id, full=full)


@app.put('/user/{user_id}/update', tags=['users'])
def update_user(user_id: int, req: User):
    if dbu.update_user(user_id, req.dict()):
        return dict(status=f'user was updated')
    else:
        return dict(status=f'internal error')

# # ----- # ----- # ----- # ----- # ----- # ----- # ----- # -----


@app.get('/user/{user_id}/schedules', tags=['schedule'])
def get_schedules(user_id: int):
    return dbs.get_schedules(_id=user_id)


@app.post('/user/{user_id}/schedules', tags=['schedule'])
def add_schedule(user_id: int, req: Schedule):
    if dbs.add_schedule(_id=user_id, title=req.dict()['title']):
        return dict(status=f'schedule was added')
    else:
        return dict(status=f'duplicate or internal error')


@app.delete('/schedule/{schedule_id}/delete', tags=['schedule'])
def add_schedule(schedule_id: int):
    if dbs.delete_schedule(_id=schedule_id):
        return dict(status=f'schedule was deleted')
    else:
        return dict(status=f'internal error')


# # ----- # ----- # ----- # ----- # ----- # ----- # ----- # -----


@app.get('/user/{user_id}/free', tags=['time slots'])
def get_free_slots_by_user_id(user_id: int):
    return dba.get_free_slots_by_user_id(_id=user_id)


@app.post('/user/{user_id}/free/add', tags=['time slots'])
def add_user_free_slots(user_id: int, req: SlotsList):
    if dba.add_user_free_slots(_id=user_id, slots_list=req.dict()['slots']):
        return dict(status=f'data was added')
    else:
        return dict(status=f'duplicate or internal error')


@app.put('/slot/{slot_id}/update', tags=['time slots'])
def update_free_slot(slot_id: int, req: Slots):
    if dba.update_free_slot(slot_id, req.dict()):
        return dict(status=f'free slot was updated')
    else:
        return dict(status=f'internal error')


@app.delete('/slot/{slot_id}/delete', tags=['time slots'])
def update_free_slot(slot_id: int):
    if dba.delete_time_slot(slot_id):
        return dict(status=f'free slot was deleted')
    else:
        return dict(status=f'internal error')

# # ----- # ----- # ----- # ----- # ----- # ----- # ----- # -----


@app.get('/user/{user_id}/busy', tags=['time slots'])
def get_busy_slots_by_user_id(user_id: int):
    return dba.get_busy_slots_by_user_id(_id=user_id)


@app.post('/user/{user_id}/busy/add', tags=['time slots'])
def add_user_busy_slots(user_id: int, req: SlotsList):
    if dba.add_user_busy_slots(_id=user_id, slots_list=req.dict()['slots']):
        return dict(status=f'data was added')
    else:
        return dict(status=f'duplicate or internal error')

# # ----- # ----- # ----- # ----- # ----- # ----- # ----- # -----


@app.get('/user/{user_id}/types', tags=['event types'])
def get_event_types_by_user_id(user_id: int, Authorize: AuthJWT = Depends()):
    # Authorize.jwt_required()
    return dbe.get_event_types_by_user_id(_id=user_id)


@app.post('/user/{user_id}/types/add', tags=['event types'])
def add_user_event_types(user_id: int, req: Type, Authorize: AuthJWT = Depends()):
    # Authorize.jwt_required()
    if dbe.add_types(_id=user_id, type_object=req.dict()):
        return dict(status=f'data was added')
    else:
        return dict(status=f'duplicate or internal error')

# # ----- # ----- # ----- # ----- # ----- # ----- # ----- # -----


@app.post('/meeting/{user_id}/add', tags=['events'])
def add_meeting(user_id: int, req: Meeting):
    if dbm.add_meeting(_id=user_id, meeting_object=req.dict()):
        return dict(status=f'data was added')
    else:
        return dict(status=f'duplicate or internal error')


@app.get('/meeting/{user_id}/all', tags=['events'])
def get_meetings(user_id: int, limit: int = 50, offset: int = 0):
    return dbm.get_meetings(user_id, limit, offset)


@app.get('/meeting/{user_id}/{meeting_id}', tags=['events'])
def get_meeting(user_id: int, meeting_id: int):
    return dbm.get_meeting(_id=meeting_id, user_id=user_id)


@app.put('/meeting/{meeting_id}/update', tags=['events'])
def update_meeting(meeting_id: int, req: Meeting):
    if dbm.update_meeting(meeting_id, req.dict()):
        return dict(status=f'meeting was updated')
    else:
        return dict(status=f'internal error')

# # ----- # ----- # ----- # ----- # ----- # ----- # ----- # -----


@app.post('/notify/new', tags=['notification'])
def notify_new(req: Notification):
    if dbn.new_event(chat_id=req.dict()['chat_id']):
        return dict(status=f'message was delivered')
    else:
        return dict(status=f'message was not delivered')


@app.post('/notify/approve', tags=['notification'])
def notify_approve(req: Notification):
    if dbn.approve_meeting(chat_id=req.dict()['chat_id']):
        return dict(status=f'message was delivered')
    else:
        return dict(status=f'message was not delivered')


@app.post('/notify/cancel', tags=['notification'])
def notify_cancel(req: Notification):
    if dbn.cancel_meeting(chat_id=req.dict()['chat_id']):
        return dict(status=f'message was delivered')
    else:
        return dict(status=f'message was not delivered')

# # ----- # ----- # ----- # ----- # ----- # ----- # ----- # -----


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=5000)
