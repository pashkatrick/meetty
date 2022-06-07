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


# {
# "title": "35 minute meeting",
# "agenda": "Partner yourself ok and write sing house.",
# "description": "Reason church individual read those song.",
# "offline": false,
# "type_id": 3,
# "recepient_name": "William Hughes",
# "recepient_email": "coolbatmanarrow@gmail.com",
# "start_time": null,
# "end_time": null,
# "year": 2022,
# "month": 5,
# "day": 13,
# "weekday": 5,
# "status": null,
# "confirmed": false,
# "rejected": false,
# "paid": false,
# "provider": ""
# }