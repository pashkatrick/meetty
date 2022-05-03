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
    schedule_id: Optional[int]


class User(BaseModel):
    name: Optional[str]
    username: Optional[str]
    avatar: Optional[str]
    bio: Optional[str]
    lang: Optional[str]
    email: Optional[str]
    created_date: Optional[str]
    password: Optional[str]
    time_zone: Optional[str]
    strat_time: Optional[str]
    theme: Optional[str]
    away: Optional[bool]
    verified: Optional[bool]
    metadata: Optional[str]
    hide_branding: Optional[bool]
    credentials: Optional[str]
    plan: Optional[str]


class SlotsList(BaseModel):
    slots: List[Slots]


class Type(BaseModel):
    default: bool
    description: str
    length: int
    slug: str
    title: str


class Meeting(BaseModel):
    title: Optional[str]
    agenda: Optional[str]
    description: Optional[str]
    offline: Optional[bool]
    type_id: Optional[int]
    recepient_name: Optional[str]
    recepient_email: Optional[str]
    start_time: Optional[int]
    end_time: Optional[int]
    year: Optional[int]
    month: Optional[int]
    day: Optional[int]
    weekday: Optional[int]
    status: Optional[int]
    confirmed: Optional[bool]
    rejected: Optional[bool]
    paid: Optional[bool]
    provider: Optional[str]


class Schedule(BaseModel):
    title: str


class Notification(BaseModel):
    chat_id: str
    # message: str
