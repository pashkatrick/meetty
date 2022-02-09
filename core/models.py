def medicine(db, orm, Age, FoodType, TimeADay, Driving, Alcohol,
             Pregnancy, SideEffect, ActiveSubstance, MedicineForm, Reason, Receiving):
    class Medicine(db.Entity):
        _id = orm.PrimaryKey(int, auto=True)
        name = orm.Required(str)
        mnn = orm.Required(ActiveSubstance)
        form = orm.Required(MedicineForm)
        ru_number = orm.Required(str)
        age = orm.Required(Age)
        side_effect = orm.Optional(SideEffect)
        food_type = orm.Optional(FoodType)
        time_a_day = orm.Optional(TimeADay)
        driving_id = orm.Optional(Driving)
        alcohol_id = orm.Optional(Alcohol)
        pregnant_id = orm.Optional(Pregnancy)
        reason_id = orm.Optional(Reason)
        receive_id = orm.Optional(Receiving)
    return Medicine


def medicine_form(db, orm):
    class MedicineForm(db.Entity):
        _id = orm.PrimaryKey(int, auto=True)
        form = orm.Required(str, 256)
        medicines = orm.Set('Medicine')
    return MedicineForm


def active_substance(db, orm):
    class ActiveSubstance(db.Entity):
        _id = orm.PrimaryKey(int, auto=True)
        substance = orm.Required(str, 256)
        medicines = orm.Set('Medicine')
    return ActiveSubstance


def side_effect(db, orm):
    class SideEffect(db.Entity):
        _id = orm.PrimaryKey(int, auto=True)
        effect = orm.Required(str, 256)
        medicines = orm.Set('Medicine')
    return SideEffect


def alcohol(db, orm):
    class Alcohol(db.Entity):
        _id = orm.PrimaryKey(int, auto=True)
        alcohol = orm.Required(str, 30)
        medicines = orm.Set('Medicine')
    return Alcohol


def pregnancy(db, orm):
    class Pregnancy(db.Entity):
        _id = orm.PrimaryKey(int, auto=True)
        pregnancy = orm.Required(str, 30)
        medicines = orm.Set('Medicine')
    return Pregnancy


def driving(db, orm):
    class Driving(db.Entity):
        _id = orm.PrimaryKey(int, auto=True)
        driving = orm.Required(str, 30)
        medicines = orm.Set('Medicine')
    return Driving


def time_a_day(db, orm):
    class TimeADay(db.Entity):
        _id = orm.PrimaryKey(int, auto=True)
        time = orm.Required(str, 10)
        medicines = orm.Set('Medicine')
    return TimeADay


def food_type(db, orm):
    class FoodType(db.Entity):
        _id = orm.PrimaryKey(int, auto=True)
        food = orm.Required(str, 10)
        medicines = orm.Set('Medicine')
    return FoodType


def age(db, orm):
    class Age(db.Entity):
        age_id = orm.PrimaryKey(int, auto=True)
        group = orm.Required(str, 10)
        medicines = orm.Set('Medicine')
    return Age


def reason(db, orm):
    class Reason(db.Entity):
        reason_id = orm.PrimaryKey(int, auto=True)
        reason = orm.Required(str, 255)
        medicines = orm.Set('Medicine')
    return Reason


def receiving(db, orm):
    class Receiving(db.Entity):
        receive_id = orm.PrimaryKey(int, auto=True)
        receive_way = orm.Required(str, 100)
        medicines = orm.Set('Medicine')
    return Receiving
