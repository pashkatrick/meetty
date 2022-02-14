from pony import orm
from pony.orm import db_session

from core.models import *


class DBController:

    def __init__(self, config):
        self.db = orm.Database()

        # self.db.bind(provider='postgres', user=config('PSQL_ROOT_USER'),
        #              password=config('PSQL_ROOT_PASS'),
        #              host=config('PSQL_HOST'),
        #              database=config('PSQL_DB'))
        self.db.bind(provider='sqlite',
                     filename='../database.sqlite', create_db=True)

        _conf = (self.db, orm)

        self.user_model = user(*_conf)
        self.meeting_model = meeting(*_conf)
        self.interest_model = interest(*_conf)
        self.source_model = source(*_conf)
        self.db.generate_mapping(create_tables=True)

    '''
    User Methods
    '''

    @db_session
    def get_user_by_id(self, _id: int, full: bool):
        try:
            usr = self.user_model[_id]
            response = usr.to_dict() if full else f'{usr.name}'
            return dict(data=response)
        except Exception as e:
            return dict(data=f'error: {e}')

    @db_session
    def get_user_by_name(self, _username: str, full: bool):
        try:
            usr = self.user_model.select(
                lambda u: _username in u.username).first()
            response = usr.to_dict() if full else f'{usr.name}'
            return dict(data=response)
        except Exception as e:
            return dict(data=f'error: {e}')

    @db_session
    def get_users(self, limit: int = 100, offset: int = 0):
        result = []
        try:
            for item in self.user_model.select()[offset:limit]:
                result.append(item.to_dict())
            return dict(data=result)
        except Exception as e:
            return dict(data=f'error: {e}')

    @db_session
    def add_user(self, user_object):
        try:
            self.user_model(**user_object)
            return dict(data='ok')
        except Exception as e:
            return dict(data=f'error: {e}')

    @db_session
    def update_user(self, update_id, update_data):
        usr = self.user_model[update_id]
        try:
            usr.set(**update_data)
            return dict(data='ok')
        except Exception as e:
            return dict(data=f'error: {e}')

    '''
    Meeting Methods
    '''

    @db_session
    def get_meeting(self, _id: int, full: bool):
        try:
            mt = self.meeting_model[_id]
            response = mt.to_dict() if full else f'{mt.link}'
            return dict(data=response)
        except Exception as e:
            return dict(data=f'error: {e}')

    @db_session
    def get_meetings(self, limit: int = 100, offset: int = 0):
        result = []
        try:
            for item in self.meeting_model.select()[offset:limit]:
                result.append(item.to_dict())
            return dict(data=result)
        except Exception as e:
            return dict(data=f'error: {e}')

    '''
    Interests Methods
    '''

    @db_session
    def get_interests(self):
        result = []
        try:
            for item in self.interest_model.select():
                result.append(item.to_dict())
            return dict(data=result)
        except Exception as e:
            return dict(data=f'error: {e}')

    '''
    Sources Methods
    '''

    @db_session
    def get_sources(self):
        result = []
        try:
            for item in self.source_model.select():
                result.append(item.to_dict())
            return dict(data=result)
        except Exception as e:
            return dict(data=f'error: {e}')
