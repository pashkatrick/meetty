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
        self.db.bind(provider='sqlite', filename='../database.sqlite', create_db=True)

        _conf = (self.db, orm)
        _model_funcs = [age, food_type, time_a_day, driving,
                        alcohol, pregnancy, side_effect, active_substance, medicine_form, reason, receiving]
        _models = []
        for _func in _model_funcs:
            _models.append(_func(*_conf))

        self.medicine_model = medicine(*_conf, *_models)
        self.db.generate_mapping(create_tables=True)

    '''
    Medicine Methods
    '''

    @db_session
    def search(self, search_query: str, limit: int = 10):
        try:
            search_results = list(self.medicine_model.select(
                lambda lc: search_query in lc.name)[:limit])
            if search_results:
                search_response = []
                for item in search_results:
                    search_response.append(item.to_dict())
                return dict(result=search_response)
            else:
                return dict(result=f'nothing found by query \'{search_query}\'')
        except Exception as e:
            return dict(result=f'error: {e}')

    @db_session
    def add_medicine(self, medicine_object):
        try:
            self.medicine_model(**medicine_object)
            return dict(result='ok')
        except Exception as e:
            return dict(result=f'error: {e}')

    @db_session
    def update_medicine(self, update_id, update_data):
        med = self.medicine_model[update_id]
        try:
            med.set(**update_data)
            return dict(result='ok')
        except Exception as e:
            return dict(result=f'error: {e}')

    @db_session
    def get_medicine(self, _id: int, full: bool):
        try:
            med = self.medicine_model[_id]
            response = med.to_dict(
            ) if full else f'{med.name}, {med.age.group}'
            return dict(result=response)
        except Exception as e:
            return dict(result=f'error: {e}')

    @db_session
    def get_medicines(self, limit: int = 100, offset: int = 0):
        result = []
        try:
            for item in self.medicine_model.select()[offset:limit]:
                result.append(item.to_dict())
            return dict(result=result)
        except Exception as e:
            return dict(result=f'error: {e}')
