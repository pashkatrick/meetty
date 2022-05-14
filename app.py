from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from fastapi import FastAPI, Depends
from fastapi.security import HTTPBearer
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from core import user_controller
from fastapi.responses import JSONResponse
from models.schemes import *
from routers import users, schedules, slots, meetings, types, notification

app = FastAPI()
dbu = user_controller.DBUserController()

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


# need for docs auth button
token_auth_scheme = HTTPBearer()


@AuthJWT.load_config
def get_config():
    return Settings()


@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request, exc: AuthJWTException):
    return JSONResponse(status_code=exc.status_code, content={'detail': exc.message})


@app.get('/', tags=['index'])
def index():
    return dict(data='Welcome to Calendario')


@app.get('/ready')
def ready(Authorize: AuthJWT = Depends(), token=Depends(token_auth_scheme)):
    Authorize.jwt_required()
    current_user = Authorize.get_jwt_subject()
    return dict(status=f'ok, {current_user}')


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


app.include_router(users.router)
app.include_router(schedules.router)
app.include_router(slots.router)
app.include_router(meetings.router)
app.include_router(types.router)
app.include_router(notification.router)


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=5000)
