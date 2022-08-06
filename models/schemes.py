from pydantic import BaseModel
from typing import List
from secrets import secret_phrase


class Settings(BaseModel):
    authjwt_secret_key: str = secret_phrase


class Auth(BaseModel):
    login: str
    password: str


class FreeSlots(BaseModel):
    day: int | None
    time_from: int | None
    time_to: int | None
    schedule_id: int | None


class BusySlots(BaseModel):
    day: int | None
    time_from: int | None
    time_to: int | None
    year: int | None
    month: int | None
    day: int | None
    weekday: int | None
    meeting_id: int | None


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


class FreeSlotsList(BaseModel):
    slots: List[FreeSlots]


class BusySlotsList(BaseModel):
    slots: List[BusySlots]


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


class Notification(BaseModel):
    reply_to: str
    subject: str
    message: str
    # attach: str
