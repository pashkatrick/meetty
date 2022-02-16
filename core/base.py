from pony import orm

from core.models import *


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
        self._availability = availability(*_conf, self._user)
        self._meeting = meeting(*_conf)
        self.db.generate_mapping(create_tables=True)
