import requests
from config import host


class TestUsers:

    # TODO: add user data check + adding user
    def test_get_user(self):
        assert requests.get(
            f'{self.host}/users?limit=20&offset=1').status_code == 200
        assert requests.get(f'{self.host}/user/6').status_code == 200
