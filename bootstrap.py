from core import completer

dbc = completer.DBCompleter()
dbc.add_users()
dbc.add_meetings()
dbc.add_events()
dbc.add_availabilities()
dbc.add_schedules()
