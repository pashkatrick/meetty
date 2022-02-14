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
    return dict(body='Welcome to Random Coffee')


@app.route('/bootstrap')
def complete():
    dbc = completer.DBCompleter(config=env_config)
    dbc.add_users()
    dbc.add_meetings()
    dbc.add_sourses()
    dbc.add_interests()
    return dict(status='ok')


# TODO: remove
@app.route('/interests/all', methods=['GET'])
def get_interests():
    return db.get_interests()


# TODO: remove
@app.route('/sources/all', methods=['GET'])
def get_sources():
    return db.get_sources()


@app.route('/users', methods=['GET'])
def get_users():
    _args = {**request.args}
    for key in _args:
        _args[key] = int(_args[key])
    return db.get_users(**_args)


@app.route('/user/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id, full=False):
    if request.args.get('full'):
        full = True
    return db.get_user_by_id(_id=user_id, full=full)


@app.route('/<username>', methods=['GET'])
@app.route('/user/<username>', methods=['GET'])
def get_user_by_name(username, full=False):
    if request.args.get('full'):
        full = True
    return db.get_user_by_name(_username=username, full=full)


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


# POST

@app.route('/user/add', methods=['POST'])
def add_user():
    user_object = request.json['user']
    return db.add_user(user_object)


@app.route('/user/update', methods=['POST'])
def update_user():
    upd_id = request.json['id']
    upd_object = request.json['update']
    return db.update_user(upd_id, upd_object)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port='5000')
