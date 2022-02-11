def user(db, orm):
    class User(db.Entity):
        _id = orm.PrimaryKey(int, auto=True)
        name = orm.Required(str)
        nick_name = orm.Required(str)
        avatar = orm.Required(str)
        bio = orm.Required(str)
        lang = orm.Required(str)
    return User


def meeting(db, orm):
    class Meeting(db.Entity):
        _id = orm.PrimaryKey(int, auto=True)
        type = orm.Required(str)
        app = orm.Required(str)
        link = orm.Required(str)
        pair = orm.Required(str)
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
