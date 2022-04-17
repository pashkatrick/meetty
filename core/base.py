from pony import orm

from models.models import *


class BaseClass(object):

    def __init__(self, config):
        self.db = orm.Database()
        # self.db.bind(provider='postgres', user=config('PSQL_ROOT_USER'),
        #              password=config('PSQL_ROOT_PASS'),
        #              host=config('PSQL_HOST'),
        #              database=config('PSQL_DB'))
        self.db.bind(provider='sqlite',
                     filename='../database.sqlite', create_db=True)

        _conf = (self.db, orm)

        self._user = user(*_conf)
        self._event_type = event_type(*_conf, self._user)
        self._schedule= schedule(*_conf, self._user)
        self._free_at = free_at(*_conf, self._user)
        self._busy_at = busy_at(*_conf, self._user)
        self._meeting = meeting(*_conf)
        self.db.generate_mapping(create_tables=True)


def exc_handler(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            print(f'error in method {func.__name__}: {e}')
            return False
    return wrapper
