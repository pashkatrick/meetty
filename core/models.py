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
        password = orm.Optional(str, hidden=True)
        time_zone = orm.Optional(str)
        strat_time = orm.Optional(str)
        theme = orm.Optional(str)
        verified = orm.Optional(bool, default=False)
        metadata = orm.Optional(str)
        hide_branding = orm.Optional(str)
        # sub models
        availabilities = orm.Set('Availability')
        schedule = orm.Optional(str)
        # meetings = orm.Set('Meeting')
        event_types = orm.Set('EventType')
        credentials = orm.Optional(str)
        plan = orm.Optional(str)
    return User


def event_type(db, orm, User):
    class EventType(db.Entity):
        _id = orm.PrimaryKey(int, auto=True)
        title = orm.Required(str)
        users = orm.Set(User)
        # meeting = orm.Set('Meeting')
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
        days = orm.Required(str, default=str([0, 1, 2, 3, 4]))
        start_time = orm.Optional(str, default='1970-01-01T09:00:00.000Z')
        end_time = orm.Optional(str, default='1970-01-01T19:00:00.000Z')
    return Availability


def meeting(db, orm):
    class Meeting(db.Entity):
        _id = orm.PrimaryKey(int, auto=True)
        uuid = orm.Required(str)
        agenda = orm.Optional(str)
        description = orm.Optional(str)
        title = orm.Optional(str)
        user_id = orm.Required(int)
        offline = orm.Optional(bool, default=0)
        type_id = orm.Required(int)
        start_time = orm.Optional(str, default='1970-01-01T10:00:00.000Z')
        end_time = orm.Optional(str, default='1970-01-01T10:30:00.000Z')
        status = orm.Optional(str)
        confirmed = orm.Optional(bool)
        rejected = orm.Optional(bool)
        paid = orm.Optional(bool)
        provider = orm.Optional(str)
    return Meeting
