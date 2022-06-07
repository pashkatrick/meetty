from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from models.schemes import *
from routers import users, schedules, slots, meetings, types, notification, auth
from secrets import origins
from fastapi import FastAPI

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
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
