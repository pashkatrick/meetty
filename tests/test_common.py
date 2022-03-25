import requests
from config import host


class TestUtiles:

    def test_utils(self):
        assert requests.get(f'{host}/').status_code == 200
        # assert requests.get(f'{self.host}/ready').status_code == 200
