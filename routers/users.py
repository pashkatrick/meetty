from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from fastapi import APIRouter, Depends, File, UploadFile, Request
from fastapi.responses import JSONResponse
from core import user_controller
from decouple import Config, RepositoryEnv
from models.schemes import User, Auth
from core.base import condition_response

# TODO: fix that 'config'
env = 'development'
dbg = 'true'
# print(f'env: {env}, debug: {dbg}')
env_config = Config(RepositoryEnv(f'./config/{env}.env'))
dbu = user_controller.DBUserController(config=env_config)
router = APIRouter()


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


@router.get('/users', tags=['users'])
def get_users(limit: int = 50, offset: int = 0):
    return dbu.get_users(limit, offset)


@router.get('/{username}', tags=['users'])
def get_user_by_name(username: str, full: bool = False):
    return dbu.get_user_by_name(_username=username, full=full)


@router.get('/user/{username}')
def get_user_by_name(username: str, full: bool = False):
    return dbu.get_user_by_name(_username=username, full=full)


@router.get('/user/id/{user_id}', tags=['users'])
def get_user_by_id(user_id: int, full: bool = False):
    return dbu.get_user_by_id(_id=user_id, full=full)


@router.put('/user/{user_id}/update', tags=['users'])
def update_user(user_id: int, req: User):
    if dbu.update_user(user_id, req.dict()):
        return dict(status=f'user was updated')
    else:
        return dict(status=f'internal error')


@router.post('/user/{user_id}/avatar/upload', tags=['avatar'])
async def upload_avatar(user_id: int, file: UploadFile = File(...)):
    file_name = file.filename
    # TODO: hardcode /avatar remove
    with open(f'./avatars/{file_name}', 'wb') as image:
        content = await file.read()
        image.write(content)
        image.close()
    # print(dict(content={'filename': file_name}, status_code=200))
    return condition_response(dbu.upload_avatar(user_id, file_name))


@router.get('/user/{user_id}/avatar', tags=['avatar'])
def get_user_avatar(user_id: int):
    # TODO: hardcode /avatar remove
    return dict(path=f'/avatars/{dbu.get_avatar(user_id)}')
