from fastapi.security import HTTPBearer, HTTPBasic
from fastapi_jwt_auth import AuthJWT
from fastapi import Depends, APIRouter
from core import user_controller
from models.schemes import *


dbu = user_controller.DBUserController()
router = APIRouter()

# need for docs auth button
token_auth_scheme = HTTPBearer()
# basic_auth_scheme = HTTPBasic()


@AuthJWT.load_config
def get_config():
    return Settings()


@router.get('/ready', tags=['auth'])
def ready(Authorize: AuthJWT = Depends(), token=Depends(token_auth_scheme)):
    Authorize.jwt_required()
    current_user = Authorize.get_jwt_subject()
    return dict(status=f'ok, {current_user}')


@router.post('/auth/signup', tags=['auth'])
def registration(req: Auth):
    user_login = req.login
    user_pass = req.password
    if dbu.sign_up(user_login, user_pass):
        return dict(status=f'user {user_login} was registered')
    else:
        return dict(data=f'user {user_login} already exist')


@router.post('/auth/signin', tags=['auth'])
def login(req: Auth, Authorize: AuthJWT = Depends()):
    user_login = req.login
    user_pass = req.password
    if dbu.sign_in(user_login, user_pass):
        access_token = Authorize.create_access_token(subject=user_login)
        return dict(token=access_token)
    else:
        return dict(data='user doesn\'t exist')
