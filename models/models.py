from calendar import weekday
from typing import Optional


def user(db, orm):
    class User(db.Entity):
        _id = orm.PrimaryKey(int, auto=True)
        name = orm.Optional(str)
        username = orm.Optional(str)
        avatar = orm.Optional(str)
        bio = orm.Optional(str)
        lang = orm.Optional(str)
        email = orm.Optional(str)
        created_date = orm.Optional(str)
        password = orm.Optional(str, hidden=True)
        time_zone = orm.Optional(str)
        strat_time = orm.Optional(str)
        theme = orm.Optional(str)
        away = orm.Optional(bool, default=False)
        verified = orm.Optional(bool, default=False)
        metadata = orm.Optional(str)
        hide_branding = orm.Optional(str)
        # sub models
        free = orm.Set('Free')
        busy = orm.Set('Busy')
        schedule = orm.Set('Schedule')
        # meetings = orm.Set('Meeting')
        event_types = orm.Set('EventType')
        credentials = orm.Optional(str)
        plan = orm.Optional(str)
    return User


def event_type(db, orm, User):
    class EventType(db.Entity):
        _id = orm.PrimaryKey(int, auto=True)
        title = orm.Optional(str)
        users = orm.Set(User)
        # meeting = orm.Set('Meeting')
        slug = orm.Optional(str)
        length = orm.Optional(int)
        description = orm.Optional(str)
        default = orm.Optional(bool, default=True)
    return EventType


def schedule(db, orm, User):
    class Schedule(db.Entity):
        _id = orm.PrimaryKey(int, auto=True, hidden=True)
        title = orm.Optional(str)
        users = orm.Set(User)
    return Schedule


def free_at(db, orm, User):
    class Free(db.Entity):
        _id = orm.PrimaryKey(int, auto=True, hidden=True)
        users = orm.Set(User)
        day = orm.Optional(int)
        time_from = orm.Optional(int)
        time_to = orm.Optional(int)
        schedule_id = orm.Optional(int)
    return Free


def busy_at(db, orm, User):
    class Busy(db.Entity):
        _id = orm.PrimaryKey(int, auto=True, hidden=True)
        users = orm.Set(User)
        day = orm.Optional(int)
        time_from = orm.Optional(int)
        time_to = orm.Optional(int)
    return Busy


def meeting(db, orm):
    class Meeting(db.Entity):
        _id = orm.PrimaryKey(int, auto=True)
        uuid = orm.Optional(str)
        title = orm.Optional(str)
        agenda = orm.Optional(str)
        description = orm.Optional(str)
        user_id = orm.Optional(int)
        offline = orm.Optional(bool, default=0)
        type_id = orm.Optional(int)
        recepient_name = orm.Optional(str)
        recepient_email = orm.Optional(str)
        start_time = orm.Optional(int)
        end_time = orm.Optional(int)
        year = orm.Optional(int)
        month = orm.Optional(int)
        day = orm.Optional(int)
        weekday = orm.Optional(int)
        status = orm.Optional(int)
        confirmed = orm.Optional(bool)
        rejected = orm.Optional(bool)
        paid = orm.Optional(bool)
        provider = orm.Optional(str)
    return Meeting
