import requests


class TestEvents:

    user_id = 8

    meeting_id = 1

    payload = {
        'title': '135 minute meeting',
        'agenda': 'Partner yourself ok and write sing house.',
        'description': 'Reason church individual read those song.',
        'offline': False,
        'type_id': 3,
        'recepient_name': 'William Hughes',
        'recepient_email': 'coolbatmanarrow@gmail.com',
        'start_time': 540,
        'end_time': 1020,
        'year': 2022,
        'month': 5,
        'day': 13,
        'weekday': 5,
        'status': 1,
        'confirmed': False,
        'rejected': False,
        'paid': False,
        'provider': ''
    }

    payload_update = {
        'title': '100500 minutes ago',
    }

    def test_create_meeting(self, url):
        response = requests.post(
            f'{url}/meeting/{self.user_id}/create?notify=false', json=self.payload)
        assert response.status_code == 200

    def test_get_meeting(self, url):
        response = requests.get(
            f'{url}/meeting/{self.user_id}/{self.meeting_id}')
        assert response.status_code == 200
        assert response.json()['meeting']

    def test_get_full_meeting(self, url):
        response = requests.get(
            f'{url}/meeting/{self.user_id}/{self.meeting_id}?full=true')
        assert response.status_code == 200

    def test_get_meetings(self, url):
        response = requests.get(
            f'{url}/meeting/{self.user_id}/all?limit=10&offset=1')
        assert response.status_code == 200

    def test_get_meetings_limit(self, url):
        response = requests.get(
            f'{url}/meeting/{self.user_id}/all?limit=2&offset=1')
        assert response.status_code == 200
        assert len(response.json()['meetings']) <= 2

    def test_update_meeting(self, url):
        response = requests.put(
            f'{url}/user/{self.meeting_id}/update', json=self.payload_update)
        assert response.status_code == 200
        response_after = requests.get(
            f'{url}/meeting/{self.user_id}/{self.meeting_id}?full=true')
        meet = response_after.json()['meeting']
        assert meet['title'] == self.payload_update['title']

    def test_cancel_meeting(self, url):
        response = requests.post(
            f'{url}/meeting/{self.meeting_id}/cancel?notify=false')
        assert response.status_code == 200
