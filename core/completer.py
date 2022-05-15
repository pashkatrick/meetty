import email
from pony.orm import db_session
from faker import Faker
from core.base import BaseClass
from models.models import *
import random
from random import randint
import uuid


class DBCompleter(BaseClass):

    def __init__(self):
        BaseClass.__init__(self)
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
        for i in range(10):
            fake_data = dict(
                title=f'{i*3}0 minute meeting',
                uuid = str(uuid.uuid4()),
                agenda=self.fake.paragraph(nb_sentences=1),
                description=self.fake.paragraph(nb_sentences=1),
                user_id=i,
                type_id=i,
                recepient_name=self.fake.name(),
                recepient_email=self.fake.email(),
                year=2022,
                month=i+2,
                day=i+10,
                weekday=randint(0, 7),
                status=randint(1, 3)
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
                users=self._user[1],
                length=15
            )
            self._event_type(
                title='30 min meeting',
                users=self._user[1],
                length=30
            )
            self._event_type(
                title='Stupid hour',
                users=self._user[2],
                length=60
            )
        except Exception as e:
            return print(f'error: {e}')
        print('----------------  events added  ----------------')

    @db_session
    def add_availabilities(self):
        for i in range(1, 10):
            try:
                self._free_at(
                    users=self._user[i],
                    day=0,
                    time_from=540,
                    time_to=1020,
                    schedule_id=i
                ),
                self._free_at(
                    users=self._user[i],
                    day=1,
                    time_from=540,
                    time_to=600,
                    schedule_id=i
                ),
                self._free_at(
                    users=self._user[i],
                    day=3,
                    time_from=630,
                    time_to=1020
                )
                self._busy_at(
                    users=self._user[i],
                    day=0,
                    time_from=540,
                    time_to=1020,
                ),
                self._busy_at(
                    users=self._user[i],
                    day=1,
                    time_from=540,
                    time_to=600,
                ),
                self._busy_at(
                    users=self._user[i],
                    day=3,
                    time_from=630,
                    time_to=1020
                )
            except Exception as e:
                return print(f'error: {e}')
        print('----------------  availabilities added  ----------------')

    @db_session
    def add_schedules(self):
        for i in range(1, 10):
            try:
                self._schedule(
                    users=self._user[i],
                    title='default'
                ),
                self._schedule(
                    users=self._user[i],
                    title='short week'
                )
            except Exception as e:
                return print(f'error: {e}')
        print('----------------  schedules added  ----------------')
