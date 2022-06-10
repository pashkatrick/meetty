from pony import orm
from models.models import *
from secrets import USER, PASS, HOST, DB


class BaseClass(object):

    def __init__(self):
        self.db = orm.Database()
        self.db.bind(provider='mysql',
                        host=HOST,
                        user=USER,
                        passwd=PASS,
                        db=DB)
        # self.db.bind(provider='sqlite',
        #                 filename='../database.sqlite', create_db=True)

        _conf = (self.db, orm)
        self._user = user(*_conf)
        self._event_type = event_type(*_conf, self._user)
        self._schedule = schedule(*_conf, self._user)
        self._free_at = free_at(*_conf, self._user)
        self._busy_at = busy_at(*_conf, self._user)
        self._meeting = meeting(*_conf)
        self.db.generate_mapping(create_tables=True)


def exc_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f'error in method {func.__name__}: {e}')
            return False
    return wrapper


def update_handler(upd_data):
    return {k: v for k, v in upd_data.items() if v is not None}


def condition_response(func):
    if func:
        return dict(status=f'successful request')
    else:
        return dict(status=f'internal error')


def mssg_response(func):
    if func:
        return dict(status=f'message was sended')
    else:
        return dict(status=f'message was not sended')
