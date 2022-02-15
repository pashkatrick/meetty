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
        self._event_type = event_type(*_conf, self._user)
        self._availablity = availability(*_conf, self._user)
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
    def add_events(self):
        try:
            self._event_type(
                title='15 min meeting',
                users=self._user.select().first(),
                length=15
            )
            self._event_type(
                title='30 min meeting',
                users=self._user.select().first(),
                length=30
            )
            self._event_type(
                title='Stupid hour',
                users=self._user.select().first(),
                length=60
            )
        except Exception as e:
            return print(f'error: {e}')
        print('----------------  events added  ----------------')

    @db_session
    def add_availabilities(self):
        for i in range(1, 10):
            try:
                self._availablity(
                    user_id=self._user[i]
                )
            except Exception as e:
                return print(f'error: {e}')
        print('----------------  availabilities added  ----------------')
