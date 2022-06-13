import requests
import pytest


class TestEventTypes:

    user_id = 7

    payload = {
        'default': False,
        'description': '',
        'length': 75,
        'slug': '75-min',
        'title': '75 min meeting'
    }

    payload_after = {
        'title': '275 min meeting'
    }

    def test_get_event_types(self, url):
        response = requests.get(f'{url}/user/{self.user_id}/types')
        data = response.json()['event_types']
        assert response.status_code == 200
        assert len(data) > 0
        assert data[0]['title']
        assert data[0]['length']
        pytest.test_event_type = data[0]['_id']

    def test_add_event_types(self, url):
        response = requests.post(
            f'{url}/user/{self.user_id}/types/add', json=self.payload)
        assert response.status_code == 200
        assert response.json()['status'] == 'successful request'

    def test_update_event_type(self, url):
        response = requests.put(
            f'{url}/type/{pytest.test_event_type}/update', json=self.payload_after)
        assert response.status_code == 200
