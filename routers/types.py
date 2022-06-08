from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from fastapi import APIRouter, Depends
from core import event_controller
from models.schemes import Type, Settings
from core.base import condition_response

dbe = event_controller.DBController()
router = APIRouter()


# @AuthJWT.load_config
# def get_config():
#     return Settings()


# @router.exception_handler(AuthJWTException)
# def authjwt_exception_handler(request, exc: AuthJWTException):
#     return JSONResponse(status_code=exc.status_code, content={'detail': exc.message})


@router.get('/user/{user_id}/types', tags=['event types'])
# def get_event_types_by_user_id(user_id: int, Authorize: AuthJWT = Depends()):
def get_event_types_by_user_id(user_id: int):
    # Authorize.jwt_required()
    return dbe.get_event_types_by_user_id(_id=user_id)


@router.post('/user/{user_id}/types/add', tags=['event types'])
def add_user_event_types(user_id: int, req: Type):
    # Authorize.jwt_required()
    return condition_response(dbe.add_types(_id=user_id, type_object=req.dict()))


@router.put('/type/{type_id}/update', tags=['event types'])
def add_user_event_types(type_id: int, req: Type):
    # Authorize.jwt_required()
    return condition_response(dbe.update_type(type_id, type_object=req.dict()))
