import requests
from config import host


class TestMeetings:

    def test_get_meetings(self):
        assert requests.get(
            f'{self.host}/meetings?limit=8&offset=1').status_code == 200
        assert requests.get(f'{self.host}/meeting/3').status_code == 200
        assert requests.get(
            f'{self.host}/meeting/3?full=true').status_code == 200
