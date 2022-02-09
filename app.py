from flask import Flask, request
from core import controller, completer
from decouple import Config, RepositoryEnv

app = Flask(__name__)
env = app.config['ENV']
dbg = app.config['DEBUG']
print(f'env: {env}, debug: {dbg}')
env_config = Config(RepositoryEnv(f'./config/{env}.env'))
db = controller.DBController(config=env_config)

# GET

@app.route('/ready')
def ready():
    return dict(status='ok')


@app.route('/')
def index():
    return dict(body='Welcome to Smart Pills')


@app.route('/complete')
def complete():
    dbc = completer.DBCompleter(config=env_config)
    dbc.add_age_groups()
    dbc.add_times_a_day()
    dbc.add_side_effects()
    dbc.add_forms()
    dbc.add_food_types()
    dbc.add_active_substance()
    dbc.add_alcohol_types()
    dbc.add_pregnancies()
    dbc.add_driving_types()
    dbc.add_reasons()
    dbc.add_receiving_ways()
    dbc.add_medicines()
    return dict(status='done')


@app.route('/search', methods=['GET'])
def search_medicine(limit=10, glue=False):
    query = request.args['q']
    if query:
        return db.search(search_query=query)
    else:
        return dict(error='you must provide a \'q\' parameter at least')


@app.route('/users', methods=['GET'])
def get_medicines():
    _args = {**request.args}
    for key in _args:
        _args[key] = int(_args[key])
    return db.get_medicines(**_args)


@app.route('/user/<int:medicine_id>', methods=['GET'])
def get_medicine(medicine_id, full=False):
    if request.args.get('full'):
        full = True
    return db.get_medicine(_id=medicine_id, full=full)

# POST


@app.route('/user/add', methods=['POST'])
def add_medicine():
    medicine_object = request.json['medicine']
    return db.add_medicine(medicine_object)


@app.route('/user/update', methods=['POST'])
def update_medicine():
    upd_id = request.json['id']
    upd_object = request.json['update']
    return db.update_medicine(upd_id, upd_object)


@app.route('/compatibility', methods=['POST'])
def is_pair_compatible():
    medcine_pair = request.json['ids']
    if len(medcine_pair) == 2:
        result = sum(medcine_pair)
        return dict(compatibility=result)
    else:
        return dict(error='you must provide a pair of medicine\'s ids')


@app.route('/contraindication', methods=['POST'])
def is_pair_contraindicated():
    medcine_pair = request.json['ids']
    if len(medcine_pair) == 2:
        result = sum(medcine_pair)
        return dict(contraindication=result)
    else:
        return dict(error='you must provide a pair of medicine\'s ids')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port='5000')
