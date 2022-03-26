from flask import Flask, request
from core import common_controller, completer, user_controller, meeting_controller
from decouple import Config, RepositoryEnv
from flasgger import Swagger, swag_from
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager
from flask_cors import CORS

app = Flask(__name__)
swagger = Swagger(app)
CORS(app)

app.config["JWT_SECRET_KEY"] = 'super-secret'  # TODO: Change this!
jwt = JWTManager(app)

env = app.config['ENV']
dbg = app.config['DEBUG']
print(f'env: {env}, debug: {dbg}')
env_config = Config(RepositoryEnv(f'./config/{env}.env'))
db = common_controller.DBController(config=env_config)
dbu = user_controller.DBUserController(config=env_config)
dbm = meeting_controller.DBMeetingController(config=env_config)


@app.route('/ready')
@jwt_required()
def ready():
    current_user = get_jwt_identity()
    return dict(status=f'ok, {current_user}')


@app.route('/')
def index():
    return dict(data='Welcome to Calendario')


# @deprecated
# @app.route('/bootstrap')
def complete():
    dbc = completer.DBCompleter(config=env_config)
    dbc.add_users()
    dbc.add_meetings()
    dbc.add_events()
    dbc.add_availabilities()
    return dict(status='ok')


@app.route('/auth/signup', methods=['POST'])
def registration():
    user_login = request.json['login']
    user_pass = request.json['password']
    if dbu.sign_up(user_login, user_pass):
        return dict(status=f'user {user_login} was registered')
    else:
        return dict(data=f'user {user_login} already exist')


@app.route('/auth/signin', methods=['POST'])
def login():
    user_login = request.json['login']
    user_pass = request.json['password']
    if dbu.sign_in(user_login, user_pass):
        access_token = create_access_token(identity=user_login)
        return dict(token=access_token)
    else:
        return dict(data='user doesn\'t exist')


# @obsolete
# @app.route('/auth/signout')
def logout():
    pass


@app.route('/users', methods=['GET'])
@swag_from('swagger/users.yml')
def get_users():
    _args = {**request.args}
    for key in _args:
        _args[key] = int(_args[key])
    return dbu.get_users(**_args)


@app.route('/<username>', methods=['GET'])
@app.route('/user/<username>', methods=['GET'])
def get_user_by_name(username, full=False):
    if request.args.get('full'):
        full = True
    return dbu.get_user_by_name(_username=username, full=full)


# @deprecated
@app.route('/user/add', methods=['POST'])
def add_user():
    user_object = request.json['user']
    return dbu.add_user(user_object)


@app.route('/user/update', methods=['PUT'])
def update_user():
    upd_id = request.json['id']
    upd_object = request.json['update']
    return dbu.update_user(upd_id, upd_object)


@app.route('/user/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id, full=False):
    if request.args.get('full'):
        full = True
    return dbu.get_user_by_id(_id=user_id, full=full)


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


@app.route('/meeting/add', methods=['POST'])
def add_meeting():
    meeting_object = request.json['meeting']
    return dbm.add_meeding(meeting_object)


@app.route('/meetings', methods=['GET'])
@swag_from('swagger/meetings.yml')
def get_meetings():
    _args = {**request.args}
    for key in _args:
        _args[key] = int(_args[key])
    return dbm.get_meetings(**_args)


@app.route('/meeting/<int:meeting_id>', methods=['GET'])
def get_meeting(meeting_id):
    return dbm.get_meeting(_id=meeting_id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port='5000')
