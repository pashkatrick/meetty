from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager
from decouple import Config, RepositoryEnv
from core import event_controller, user_controller, meeting_controller, availability_controller
from fastapi import FastAPI
import uvicorn

# from flask import Flask, request
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)

# app.config["JWT_SECRET_KEY"] = 'super-secret'  # TODO: Change this!
# jwt = JWTManager(app)

app = FastAPI()


@app.get('/')
def root():
    return {"message": "Hello World"}


env = 'development'
dbg = 'true'
print(f'env: {env}, debug: {dbg}')
env_config = Config(RepositoryEnv(f'./config/{env}.env'))
dbe = event_controller.DBController(config=env_config)
dbu = user_controller.DBUserController(config=env_config)
dbm = meeting_controller.DBMeetingController(config=env_config)
dba = availability_controller.DBTimeController(config=env_config)


# @app.get('/ready')
# @jwt_required()
# def ready():
#     current_user = get_jwt_identity()
#     return dict(status=f'ok, {current_user}')


@app.get('/')
def index():
    return dict(data='Welcome to Calendario')

# @app.post('/auth/signup')
# def registration():
#     # user_login = request.json['login']
#     # user_pass = request.json['password']
#     if dbu.sign_up(user_login, user_pass):
#         return dict(status=f'user {user_login} was registered')
#     else:
#         return dict(data=f'user {user_login} already exist')


# @app.route('/auth/signin', methods=['POST'])
# def login():
#     user_login = request.json['login']
#     user_pass = request.json['password']
#     if dbu.sign_in(user_login, user_pass):
#         access_token = create_access_token(identity=user_login)
#         return dict(token=access_token)
#     else:
#         return dict(data='user doesn\'t exist')


@app.get('/users')
def get_users(limit: int = 50, offset: int = 0):
    return dbu.get_users(limit, offset)


@app.get('/<username>')
@app.get('/user/<username>')
def get_user_by_name(username: str, full: bool = False):
    return dbu.get_user_by_name(_username=username, full=full)


# @app.route('/user/update', methods=['PUT'])
# def update_user():
#     upd_id = request.json['id']
#     upd_object = request.json['update']
#     return dbu.update_user(upd_id, upd_object)


@app.get('/user/{user_id}')
def get_user_by_id(user_id: int, full: bool = False):
    return dbu.get_user_by_id(_id=user_id, full=full)

# # ----- # ----- # ----- # ----- # ----- # ----- # ----- # -----


@app.get('/user/{user_id}/free')
def get_free_slots_by_user_id(user_id: int):
    return dba.get_free_slots_by_user_id(_id=user_id)


# @app.route('/user/<int:user_id>/free/add', methods=['POST'])
# def add_user_free_slots(user_id):
#     if dba.add_user_free_slots(_id=user_id, slots_list=request.json['slots']):
#         return dict(status=f'data was added')
#     else:
#         return dict(status=f'duplicate or internal error')

# # ----- # ----- # ----- # ----- # ----- # ----- # ----- # -----


# @app.route('/user/<int:user_id>/busy', methods=['GET'])
# def get_busy_slots_by_user_id(user_id):
#     # return dba.get_busy_slots_by_user_id(_id=user_id)
#     pass


# @app.route('/user/<int:user_id>/busy/add', methods=['POST'])
# def add_user_busy_slots(user_id):
#     # if dba.add_user_busy_slots(_id=user_id, slots_list=request.json['slots']):
#     #     return dict(status=f'data was added')
#     # else:
#     #     return dict(status=f'duplicate or internal error')
#     pass

# # ----- # ----- # ----- # ----- # ----- # ----- # ----- # -----


@app.get('/user/{user_id}/types')
def get_event_types_by_user_id(user_id: int):
    return dbe.get_event_types_by_user_id(_id=user_id)


# @app.route('/user/<int:user_id>/types/add', methods=['POST'])
# def add_user_event_types(user_id):
#     return dbe.add_types(_id=user_id, type_object=request.json['types'])

# # ----- # ----- # ----- # ----- # ----- # ----- # ----- # -----


# @app.route('/meeting/add', methods=['POST'])
# def add_meeting():
#     meeting_object = request.json['meeting']
#     return dbm.add_meeding(meeting_object)


@app.get('/meetings')
def get_meetings(limit: int = 50, offset: int = 0):
    return dbm.get_meetings(limit, offset)


@app.get('/meeting/{meeting_id}')
def get_meeting(meeting_id: int):
    return dbm.get_meeting(_id=meeting_id)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
