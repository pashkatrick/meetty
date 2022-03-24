from core import completer
from decouple import Config, RepositoryEnv

env = 'development'
env_config = Config(RepositoryEnv(f'./config/{env}.env'))
dbc = completer.DBCompleter(config=env_config)
dbc.add_users()
dbc.add_meetings()
dbc.add_events()
dbc.add_availabilities()