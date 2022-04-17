import requests
from config import host


class TestSchedules:

    payload = {
        "title": "that's a test",
    }

    def test_get_schedules(self):
        response = requests.get(f'{host}/user/2/schedules')
        data = response.json()['schedules']
        print(data)
        assert response.status_code == 200
        assert len(data) > 0
        assert data[0]['title']
        assert data[0]['free_slots']

    def test_add_schedules(self):
        response = requests.post(f'{host}/user/2/schedules', json=self.payload)
        assert response.status_code == 200
        assert response.json()['status'] == 'schedule was added'
