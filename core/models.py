from email.policy import default
from pydoc import describe


def user(db, orm):
    class User(db.Entity):
        _id = orm.PrimaryKey(int, auto=True)
        name = orm.Required(str)
        username = orm.Optional(str)
        avatar = orm.Optional(str)
        bio = orm.Optional(str)
        lang = orm.Optional(str)
        email = orm.Optional(str)
        created_date = orm.Optional(str)
        password = orm.Optional(str)
        time_zone = orm.Optional(str)
        strat_time = orm.Optional(str)
        theme = orm.Optional(str)
        verified = orm.Optional(bool, default=False)
        metadata = orm.Optional(str)
        hide_branding = orm.Optional(str)
        # sub models
        availability_id = orm.Set('Availability')
        # availability = orm.Set(Availability)
        schedule = orm.Optional(str)
        booking = orm.Optional(str)
        event_types = orm.Set('EventType')
        credentials = orm.Optional(str)
        plan = orm.Optional(str)
    return User


def event_type(db, orm, User):
    class EventType(db.Entity):
        _id = orm.PrimaryKey(int, auto=True)
        title = orm.Required(str)
        users = orm.Set(User)
        slug = orm.Optional(str)
        length = orm.Required(int)
        description = orm.Optional(str)
        default = orm.Optional(bool, default=True)
    return EventType

# TODO: rename
def availability(db, orm, User):
    class Availability(db.Entity):
        _id = orm.PrimaryKey(int, auto=True)
        label = orm.Optional(str)
        users = orm.Set(User)
        days = orm.Required(str, default=str([0,1,2,3,4]))
        start_time = orm.Optional(str, default='1970-01-01T09:00:00.000Z')
        end_time = orm.Optional(str, default='1970-01-01T19:00:00.000Z')
    return Availability


def meeting(db, orm):
    class Meeting(db.Entity):
        _id = orm.PrimaryKey(int, auto=True)
        type = orm.Required(str)
        app = orm.Optional(str)
        link = orm.Optional(str)
        pair = orm.Optional(str)
    return Meeting
