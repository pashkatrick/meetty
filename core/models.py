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
        emailVerified = orm.Optional(str)
        password = orm.Optional(str)
        time_zone = orm.Optional(str)
        strat_time = orm.Optional(str)
        theme = orm.Optional(str)
        verified = orm.Optional(str)
        metadata = orm.Optional(str)
        hideBranding = orm.Optional(str)
        # sub models
        # availability_id = orm.Optinal(Availability)
        # availability = orm.Set(Availability)
        schedule = orm.Optional(str)
        booking = orm.Optional(str)
        # event_types = orm.Optinal(EventType)
        credentials = orm.Optional(str)
        plan = orm.Optional(str)
    return User


def availability(db, orm, User, EventType):
    class Availability(db.Entity):
        _id = orm.PrimaryKey(int, auto=True)
        user_id = orm.Optinal(User)
        # user = orm.Set(User)
        label = orm.Optional(str)
        event_type = orm.Optinal(EventType)
    return Availability


def event_type(db, orm):
    class EventType(db.Entity):
        _id = orm.PrimaryKey(int, auto=True)
    return EventType


# TODO: remove
def meeting(db, orm):
    class Meeting(db.Entity):
        _id = orm.PrimaryKey(int, auto=True)
        type = orm.Required(str)
        app = orm.Optional(str)
        link = orm.Optional(str)
        pair = orm.Optional(str)
    return Meeting


# TODO: remove
def interest(db, orm):
    class Interest(db.Entity):
        _id = orm.PrimaryKey(int, auto=True)
        name = orm.Required(str)
    return Interest


# TODO: remove
def source(db, orm):
    class Source(db.Entity):
        _id = orm.PrimaryKey(int, auto=True)
        name = orm.Required(str)
    return Source
