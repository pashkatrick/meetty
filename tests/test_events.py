import requests
from config import host


class TestEvents:

    def test_get_meeting(self):
        response = requests.get(f'{host}/meeting/3/2')
        assert response.status_code == 200

    def test_get_meetings(self):
        response = requests.get(f'{host}/meetings?limit=8&offset=1')
        assert response.status_code == 200

    def test_get_full_meeting(self):
        response = requests.get(f'{host}/meeting/3/2?full=true')
        assert response.status_code == 200

    # def test_add_meeting(self):
    #     pass
