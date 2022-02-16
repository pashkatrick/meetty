from flask import Flask, request
from core import controller, completer
from decouple import Config, RepositoryEnv

from core.models import user

app = Flask(__name__)
env = app.config['ENV']
dbg = app.config['DEBUG']
print(f'env: {env}, debug: {dbg}')
env_config = Config(RepositoryEnv(f'./config/{env}.env'))
db = controller.DBController(config=env_config)


@app.route('/ready')
def ready():
    return dict(status='ok')


@app.route('/')
def index():
    return dict(body='Welcome to Calendario')


@app.route('/bootstrap')
def complete():
    dbc = completer.DBCompleter(config=env_config)
    dbc.add_users()
    dbc.add_meetings()
    dbc.add_events()
    dbc.add_availabilities()
    return dict(status='ok')


@app.route('/users', methods=['GET'])
def get_users():
    _args = {**request.args}
    for key in _args:
        _args[key] = int(_args[key])
    return db.get_users(**_args)


@app.route('/<username>', methods=['GET'])
@app.route('/user/<username>', methods=['GET'])
def get_user_by_name(username, full=False):
    if request.args.get('full'):
        full = True
    return db.get_user_by_name(_username=username, full=full)


@app.route('/user/add', methods=['POST'])
def add_user():
    user_object = request.json['user']
    return db.add_user(user_object)


@app.route('/user/update', methods=['PUT'])
def update_user():
    upd_id = request.json['id']
    upd_object = request.json['update']
    return db.update_user(upd_id, upd_object)


@app.route('/user/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id, full=False):
    if request.args.get('full'):
        full = True
    return db.get_user_by_id(_id=user_id, full=full)


@app.route('/user/<int:user_id>/days', methods=['GET'])
def get_days_by_user_id(user_id):
    return db.get_days_by_user_id(_id=user_id)


@app.route('/user/<int:user_id>/days/add', methods=['POST'])
def add_user_days(user_id):
    return db.add_days(_id=user_id, day_object=request.json['days'])


@app.route('/user/<int:user_id>/types', methods=['GET'])
def get_event_types_by_user_id(user_id):
    return db.get_event_types_by_user_id(_id=user_id)


@app.route('/user/<int:user_id>/types/add', methods=['POST'])
def add_user_event_types(user_id):
    return db.add_types(_id=user_id, type_object=request.json['types'])


@app.route('/meetings', methods=['GET'])
def get_meetings():
    _args = {**request.args}
    for key in _args:
        _args[key] = int(_args[key])
    return db.get_meetings(**_args)


@app.route('/meeting/<int:meeting_id>', methods=['GET'])
def get_meeting(meeting_id, full=True):
    if request.args.get('full'):
        full = True
    return db.get_meeting(_id=meeting_id, full=full)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port='5000')
