from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from decouple import Config, RepositoryEnv
from core import event_controller, user_controller, meeting_controller, availability_controller
from fastapi import FastAPI, Depends
import uvicorn

from pydantic import BaseModel


class User(BaseModel):
    login: str
    password: str


class Settings(BaseModel):
    authjwt_secret_key: str = 'top-secret'


app = FastAPI()


@AuthJWT.load_config
def get_config():
    return Settings()


env = 'development'
dbg = 'true'
print(f'env: {env}, debug: {dbg}')
env_config = Config(RepositoryEnv(f'./config/{env}.env'))
dbe = event_controller.DBController(config=env_config)
dbu = user_controller.DBUserController(config=env_config)
dbm = meeting_controller.DBMeetingController(config=env_config)
dba = availability_controller.DBTimeController(config=env_config)


@app.get('/ready')
def ready(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    current_user = Authorize.get_jwt_subject()
    return dict(status=f'ok, {current_user}')


@app.get('/', tags=['index'])
def index():
    return dict(data='Welcome to Calendario')


@app.post('/auth/signup', tags=['auth'])
def registration(req: User):
    user_login = req.login
    user_pass = req.password
    if dbu.sign_up(user_login, user_pass):
        return dict(status=f'user {user_login} was registered')
    else:
        return dict(data=f'user {user_login} already exist')


@app.post('/auth/signin', tags=['auth'])
def login(req: User, Authorize: AuthJWT = Depends()):
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


# @app.put('/user/update', tags=['users'])
# def update_user(request: Request):
#     upd_id = request.json()['id']
#     upd_object = request.json()['update']
#     return dbu.update_user(upd_id, upd_object)

# # ----- # ----- # ----- # ----- # ----- # ----- # ----- # -----


@app.get('/user/{user_id}/free', tags=['time slots'])
def get_free_slots_by_user_id(user_id: int):
    return dba.get_free_slots_by_user_id(_id=user_id)


# @app.post('/user/{user_id}/free/add', tags=['time slots'])
# def add_user_free_slots(user_id: int, request: Request):
#     if dba.add_user_free_slots(_id=user_id, slots_list=request.slots):
#         return dict(status=f'data was added')
#     else:
#         return dict(status=f'duplicate or internal error')

# # ----- # ----- # ----- # ----- # ----- # ----- # ----- # -----


# @app.get('/user/<int:user_id>/busy', tags=['time slots'])
# def get_busy_slots_by_user_id(user_id):
#     # return dba.get_busy_slots_by_user_id(_id=user_id)
#     pass


# @app.post('/user/<int:user_id>/busy/add', tags=['time slots'])
# def add_user_busy_slots(user_id):
#     # if dba.add_user_busy_slots(_id=user_id, slots_list=request.json()['slots']):
#     #     return dict(status=f'data was added')
#     # else:
#     #     return dict(status=f'duplicate or internal error')
#     pass

# # ----- # ----- # ----- # ----- # ----- # ----- # ----- # -----


@app.get('/user/{user_id}/types', tags=['events'])
def get_event_types_by_user_id(user_id: int):
    return dbe.get_event_types_by_user_id(_id=user_id)


# @app.post('/user/{user_id}/types/add', tags=['events'])
# def add_user_event_types(user_id: int, request: Request):
#     return dbe.add_types(_id=user_id, type_object=request.json()['types'])

# # ----- # ----- # ----- # ----- # ----- # ----- # ----- # -----


# @app.post('/meeting/add', tags=['events'])
# def add_meeting(request: Request):
#     meeting_object = request.json()['meeting']
#     return dbm.add_meeding(meeting_object)


@app.get('/meetings', tags=['events'])
def get_meetings(limit: int = 50, offset: int = 0):
    return dbm.get_meetings(limit, offset)


@app.get('/meeting/{meeting_id}', tags=['events'])
def get_meeting(meeting_id: int):
    return dbm.get_meeting(_id=meeting_id)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
