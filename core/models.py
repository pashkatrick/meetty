def user(db, orm):
    class User(db.Entity):
        _id = orm.PrimaryKey(int, auto=True)
        name = orm.Required(str)
        nick_name = orm.Optional(str)
        avatar = orm.Optional(str)
        bio = orm.Optional(str)
        lang = orm.Optional(str)
    return User


def meeting(db, orm):
    class Meeting(db.Entity):
        _id = orm.PrimaryKey(int, auto=True)
        type = orm.Required(str)
        app = orm.Optional(str)
        link = orm.Optional(str)
        pair = orm.Optional(str)
    return Meeting


def interest(db, orm):
    class Interest(db.Entity):
        _id = orm.PrimaryKey(int, auto=True)
        name = orm.Required(str)
    return Interest


def source(db, orm):
    class Source(db.Entity):
        _id = orm.PrimaryKey(int, auto=True)
        name = orm.Required(str)
    return Source
