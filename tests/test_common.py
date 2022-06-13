import requests


class TestUtiles:

    def test_utils(self, url):
        assert requests.get(f'{url}/').status_code == 200
