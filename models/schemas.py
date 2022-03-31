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
    start_time: int
    end_time: int
    offline: bool
    paid: bool
    type_id: int
    user_id: int
