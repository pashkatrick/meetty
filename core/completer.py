from pony import orm
from pony.orm import db_session
from faker import Faker
from core.models import *


class DBCompleter:

    def __init__(self, config):

        db = orm.Database()
        # db.bind(provider=config('PROVIDER'), user=config('PSQL_ROOT_USER'),
        #         password=config('PSQL_ROOT_PASS'),
        #         host=config('PSQL_HOST'),
        #         database=config('PSQL_DB'))
        self.db.bind(provider='sqlite', filename='../database.sqlite', create_db=True)                

        _conf = (db, orm)

        self._age = age(*_conf)
        self._food = food_type(*_conf)
        self._time = time_a_day(*_conf)
        self._drive = driving(*_conf)
        self._alco = alcohol(*_conf)
        self._pregnant = pregnancy(*_conf)
        self._side_effect = side_effect(*_conf)
        self._active_substance = active_substance(*_conf)
        self._form = medicine_form(*_conf)
        self._reason = reason(*_conf)
        self._receiving = receiving(*_conf)
        self._medicine = medicine(*_conf, self._age, self._food, self._time, self._drive,
                                  self._alco, self._pregnant, self._side_effect, self._active_substance,
                                  self._form, self._reason, self._receiving)

        db.generate_mapping(create_tables=True)
        self.fake = Faker()

    @db_session
    def add_medicines(self):
        for _ in range(10):
            fake_data = dict(
                name=self.fake.bothify(text='LC: ????-??##'),
                mnn=self.fake.random_int(min=1, max=10),
                form=self.fake.random_int(min=1, max=10),
                ru_number=self.fake.bothify(text='No: ##'),
                age=self.fake.random_int(min=1, max=10),
                side_effect=self.fake.random_int(min=1, max=10),
                food_type=self.fake.random_int(min=1, max=3),
                time_a_day=self.fake.random_int(min=1, max=2),
                driving_id=self.fake.random_int(min=1, max=3),
                alcohol_id=self.fake.random_int(min=1, max=3),
                pregnant_id=self.fake.random_int(min=1, max=3),
                reason_id=self.fake.random_int(min=1, max=10),
                receive_id=self.fake.random_int(min=1, max=10)
            )
            try:
                self._medicine(**fake_data)
            except Exception as e:
                return print(f'error: {e}')
        print('----------------  medicines added  ----------------')

    @db_session
    def add_side_effects(self):
        for _ in range(10):
            try:
                self._side_effect(effect=self.fake.bothify(
                    text='effect: ????-########'))
            except Exception as e:
                return print(f'error: {e}')
        print('----------------  side effects added  ----------------')

    @db_session
    def add_age_groups(self):
        for _ in range(10):
            try:
                self._age(group=self.fake.bothify(text='##-## лет'))
            except Exception as e:
                return print(f'error: {e}')
        print('----------------  ages group added  ----------------')

    @db_session
    def add_times_a_day(self):
        try:
            self._time(time='утро')
            self._time(time='вечер')
        except Exception as e:
            return print(f'error: {e}')
        print('----------------  times added  ----------------')

    @db_session
    def add_food_types(self):
        try:
            self._food(food='до')
            self._food(food='после')
            self._food(food='во время')
        except Exception as e:
            return print(f'error: {e}')
        print('----------------  foods added  ----------------')

    @db_session
    def add_driving_types(self):
        try:
            self._drive(driving='разрешено')
            self._drive(driving='запрещено')
            self._drive(driving='с осторожностью')
        except Exception as e:
            return print(f'error: {e}')
        print('----------------  drives added  ----------------')

    @db_session
    def add_alcohol_types(self):
        try:
            self._alco(alcohol='разрешено')
            self._alco(alcohol='запрещено')
            self._alco(alcohol='с осторожностью')
        except Exception as e:
            return print(f'error: {e}')
        print('----------------  alcos added  ----------------')

    @db_session
    def add_pregnancies(self):
        try:
            self._pregnant(pregnancy='разрешено')
            self._pregnant(pregnancy='запрещено')
            self._pregnant(pregnancy='с осторожностью')
        except Exception as e:
            return print(f'error: {e}')
        print('----------------  pregnancies added  ----------------')

    @db_session
    def add_reasons(self):
        for _ in range(10):
            try:
                self._reason(reason=self.fake.bothify(
                    text='reason: ????-########'))
            except Exception as e:
                return print(f'error: {e}')
        print('----------------  reasons added  ----------------')

    @db_session
    def add_forms(self):
        for _ in range(10):
            try:
                self._form(form=self.fake.bothify(text='form: ????-########'))
            except Exception as e:
                return print(f'error: {e}')
        print('----------------  forms added  ----------------')

    @db_session
    def add_active_substance(self):
        for _ in range(10):
            try:
                self._active_substance(substance=self.fake.bothify(
                    text='substance: ????-########'))
            except Exception as e:
                return print(f'error: {e}')
        print('----------------  active substance added  ----------------')

    @db_session
    def add_reasons(self):
        for _ in range(10):
            try:
                self._reason(reason=self.fake.bothify(
                    text='reason: ????-######'))
            except Exception as e:
                return print(f'error: {e}')
        print('----------------  reasons added  ----------------')

    @db_session
    def add_receiving_ways(self):
        try:
            self._receiving(
                receive_way='Внутрь (перорально, через рот) (peros)')
            self._receiving(receive_way='Под язык (сублингвально) (sublingua)')
            self._receiving(receive_way='За щеку (трансбуккально)')
            self._receiving(receive_way='В 12-перстную кишку (дуоденально)')
            self._receiving(receive_way='В прямую кишку (ректально)')
            self._receiving(receive_way='Подкожно')
            self._receiving(receive_way='Внутримышечно')
            self._receiving(receive_way='Внутривенно')
            self._receiving(receive_way='Внутриартериално')
            self._receiving(receive_way='Внутрибрюшинно')
            self._receiving(receive_way='Внутриплеврально')
            self._receiving(receive_way='Субарахноидально')
            self._receiving(receive_way='Интрацистернального')
            self._receiving(receive_way='Внутрисердечно')
            self._receiving(receive_way='В полость суставов')
            self._receiving(receive_way='Субокципитально')
            self._receiving(receive_way='Накожно (трансдермально)')
            self._receiving(receive_way='Ингаляционно')
            self._receiving(receive_way='Интраназально')
            self._receiving(receive_way='Ионофоретически')
        except Exception as e:
            return print(f'error: {e}')
        print('----------------  receiving ways added  ----------------')
