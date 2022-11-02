from pprint import pprint
from fastapi.security import HTTPBearer
from fastapi_jwt_auth import AuthJWT
from fastapi import Depends, APIRouter
from core import user_controller
from models.schemes import Settings, Auth


dbu = user_controller.DBUserController()
router = APIRouter()

# need for docs auth button
token_auth_scheme = HTTPBearer()


@AuthJWT.load_config
def get_config():
    return Settings()


@router.get('/ready', tags=['auth'])
def ready(Authorize: AuthJWT = Depends(), token=Depends(token_auth_scheme)):
    Authorize.jwt_required()
    current_user = Authorize.get_jwt_subject()
    return dict(status=f'ok, {current_user}')


@router.post('/auth/signin', tags=['auth'])
def login(req: Auth, Authorize: AuthJWT = Depends()):
    user_login = req.login
    user_pass = req.password
    user_id = dbu.sign_in(user_login, user_pass)
    if user_id:
        access_token = Authorize.create_access_token(subject=user_login)
        return dict(user_id=user_id, token=access_token)
    else:
        return dict(data='user doesn\'t exist')


@router.post('/auth/signup', tags=['auth'])
def registration(req: Auth):
    user_login = req.login
    user_pass = req.password
    user_id = dbu.sign_up(user_login, user_pass)
    if user_id:
        return dict(user_id=user_id, status=f'user {user_login} was registered')
    else:
        return dict(data='Something wrong or user already exist')


@router.get('/auth/check', tags=['auth'])
def check_user(email: str):
    check = dbu.is_user_exist(email)
    pprint(check)
    if check:
        return dict(user_id=check._id, email=email, exist=True)
    else:
        return dict(user=email, exist=False)
