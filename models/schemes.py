from pydantic import BaseModel
from typing import List
from typing import Optional


class Settings(BaseModel):
    authjwt_secret_key: str = 'top-secret'


class Auth(BaseModel):
    login: str
    password: str


class Slots(BaseModel):
    day: int
    time_from: int
    time_to: int
    schedule_id: int | None
    year: int | None
    month: int | None
    day: int | None
    weekday: int | None    


class User(BaseModel):
    name: str | None
    username: str | None
    avatar: str | None
    bio: str | None
    lang: str | None
    email: str | None
    created_date: str | None
    password: str | None
    time_zone: str | None
    strat_time: str | None
    theme: str | None
    away: bool | None
    verified: bool | None
    metadata: str | None
    hide_branding: bool | None
    credentials: str | None
    plan: str | None


class SlotsList(BaseModel):
    slots: List[Slots]


class Type(BaseModel):
    default: bool | None
    description: str | None
    length: int | None
    slug: str | None
    title: str | None


class Meeting(BaseModel):
    title: str | None
    agenda: str | None
    description: str | None
    offline: bool | None
    type_id: int | None
    recepient_name: str | None
    recepient_email: str | None
    start_time: int | None
    end_time: int | None
    year: int | None
    month: int | None
    day: int | None
    weekday: int | None
    status: int | None
    confirmed: bool | None
    rejected: bool | None
    paid: bool | None
    provider: str | None


class Schedule(BaseModel):
    title: str
    default: bool = False


class Notification(BaseModel):
    chat_id: str
    # message: str
