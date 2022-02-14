from pony import orm
from pony.orm import db_session
from faker import Faker
from core.models import *
import random


class DBCompleter:

    def __init__(self, config):

        db = orm.Database()
        # db.bind(provider=config('PROVIDER'), user=config('PSQL_ROOT_USER'),
        #         password=config('PSQL_ROOT_PASS'),
        #         host=config('PSQL_HOST'),
        #         database=config('PSQL_DB'))
        db.bind(provider='sqlite', filename='../database.sqlite', create_db=True)

        _conf = (db, orm)
        self._user = user(*_conf)
        self._source = source(*_conf)
        self._interest = interest(*_conf)
        self._meeting = meeting(*_conf)

        db.generate_mapping(create_tables=True)
        self.fake = Faker()

    @db_session
    def add_users(self):
        for _ in range(10):
            fake_data = dict(
                name=self.fake.name(),
                username=self.fake.simple_profile()['username'],
                avatar='file://<path>/',
                bio=self.fake.paragraph(nb_sentences=1),
                lang=random.choice(['ru', 'en', 'gb', 'us'])
            )
            try:
                self._user(**fake_data)
            except Exception as e:
                return print(f'error: {e}')
        print('----------------  users added  ----------------')

    @db_session
    def add_meetings(self):
        for i in range(5):
            fake_data = dict(
                type=random.choice(['offline', 'online']),
                app=random.choice(['zoom', 'google', 'skype']),
                link='https://app.host/<path>/',
                pair=f'{i},{i+1}'
            )
            try:
                self._meeting(**fake_data)
            except Exception as e:
                return print(f'error: {e}')
        print('----------------  meetings added  ----------------')

    @db_session
    def add_interests(self):
        try:
            self._interest(name='polo')
            self._interest(name='marketing')
            self._interest(name='sweets')
            self._interest(name='books')
            self._interest(name='travel')
        except Exception as e:
            return print(f'error: {e}')
        print('----------------  interests added  ----------------')

    @db_session
    def add_sourses(self):
        try:
            self._source(name='skype')
            self._source(name='zoom')
            self._source(name='google')
        except Exception as e:
            return print(f'error: {e}')
        print('----------------  sourses added  ----------------')
