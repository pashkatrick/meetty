from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from models.schemes import *
from routers import users, schedules, slots, meetings, types, notification, auth
from secrets import origins, OPENAPI_URL
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi_jwt_auth.exceptions import AuthJWTException
from fastapi import Request

app = FastAPI(openapi_url=OPENAPI_URL)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )


@app.get('/', tags=['index'])
def index():
    return dict(data='Welcome to Meetty')


app.include_router(auth.router)
app.include_router(users.router)
app.include_router(schedules.router)
app.include_router(slots.router)
app.include_router(meetings.router)
app.include_router(types.router)
app.include_router(notification.router)


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=5000)
