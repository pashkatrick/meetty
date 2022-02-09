def collection(db, orm):
    class Collection(db.Entity):
        Id = orm.PrimaryKey(int, auto=True)
        Name = orm.Optional(str, 100)
        queries = orm.Set('Item')
    return Collection


def item(db, orm, Collection):
    class Item(db.Entity):
        Id = orm.PrimaryKey(int, auto=True)
        Name = orm.Optional(str)
        Host = orm.Optional(str)
        Method = orm.Optional(str)
        Request = orm.Optional(str)
        Meta = orm.Optional(str)
        Collection_id = orm.Required(Collection)
    return Item

def medicine(db, orm):
    class Medicine(db.Entity):
        _id = orm.PrimaryKey(int, auto=True)
        name = orm.Optional(str)
        dosage_form = orm.Optional(str)
        dosage_grls = orm.Optional(str)
        ru_number = orm.Optional(str)
        age_category = orm.Optional(str)
        break_between_receptions = orm.Optional(str)
        dosage = orm.Optional(str)
        meal_time = orm.Optional(str)
    return Medicine