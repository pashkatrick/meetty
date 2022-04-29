from pydantic import BaseModel
from typing import List


class Settings(BaseModel):
    authjwt_secret_key: str = 'top-secret'


class Auth(BaseModel):
    login: str
    password: str


class Slots(BaseModel):
    day: int
    time_from: int
    time_to: int


class SlotsList(BaseModel):
    slots: List[Slots]


class Type(BaseModel):
    default: bool
    description: str
    length: int
    slug: str
    title: str


class Meeting(BaseModel):
    title: str
    agenda: str
    description: str
    offline: bool
    type_id: int
    recepient_name: str
    recepient_email: str
    start_time: int
    end_time: int
    year: int
    month: int
    day: int
    weekday: int
    status: int
    confirmed: bool
    rejected: bool
    paid: bool
    provider: str


class Schedule(BaseModel):
    title: str


class Notification(BaseModel):
    chat_id: str
    # message: str
