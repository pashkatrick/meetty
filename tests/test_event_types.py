import requests
from config import host


class TestEventTypes:

    payload = {
        "default": False,
        "description": "",
        "length": 75,
        "slug": "75-min",
        "title": "75 min meeting"
    }

    def test_get_event_types(self):
        response = requests.get(f'{host}/user/2/types')
        data = response.json()['data']
        assert response.status_code == 200
        assert len(data) > 0
        assert data[0]['title']
        assert data[0]['length']

    def test_add_event_types(self):
        response = requests.post(f'{host}/user/2/types/add', json=self.payload)
        assert response.status_code == 200
        assert response.json()['status'] == 'data was added'
