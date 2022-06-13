from urllib import response
import requests
import pytest


class TestSchedules:

    user_id = 2
    payload = {
        'title': 'that\'s a test',
    }

    payload_update = {
        'title': 'that\s was a test',
    }

    def test_add_schedules(self, url):
        response = requests.post(
            f'{url}/user/{self.user_id}/schedules', json=self.payload)
        assert response.status_code == 200
        assert response.json()['status'] == 'successful request'

    def test_get_schedules(self, url):
        response = requests.get(f'{url}/user/{self.user_id}/schedules')
        data = response.json()['schedules']
        assert response.status_code == 200
        assert len(data) > 0
        assert data[0]['title']
        assert data[0]['free_slots']
        pytest.test_slot_id = data[-1]['_id']

    def test_update_schdule(self, url):
        response = requests.put(
            f'{url}/user/{self.user_id}/schedule/{pytest.test_slot_id}/update', json=self.payload_update)
        assert response.status_code == 200

    def test_delete_schdule(self, url):
        response = requests.delete(
            f'{url}/schedule/{pytest.test_slot_id}/delete', json={'schedule_id': pytest.test_slot_id})
        assert response.status_code == 200
