import requests
import pytest


class TestUsers():

    user_id = 6
    payload_update = {
        'name': 'Borov Barabeq',
        'username': 'barabeq',
        'away': True
    }

    def test_get_users(self, url):
        response = requests.get(
            f'{url}/users?limit=20&offset=1')
        assert response.status_code == 200
        assert len(response.json()['users'][0]) >= 10

    def test_get_users_limit(self, url):
        response = requests.get(
            f'{url}/users?limit=9&offset=1')
        assert response.status_code == 200
        assert len(response.json()['users']) <= 9

    def test_get_user_by_id(self, url):
        response = requests.get(f'{url}/user/id/{self.user_id}')
        assert response.status_code == 200
        assert response.json()['user']

    def test_get_full_user(self, url):
        response = requests.get(f'{url}/user/id/{self.user_id}?full=true')
        user = response.json()['user']
        assert response.status_code == 200
        assert user
        pytest.test_username = user['username']
        pytest.test_name = user['name']

    def test_get_user_by_username(self, url):
        response = requests.get(f'{url}/{pytest.test_username}')
        assert response.json()['user'] == pytest.test_name

    def test_update_user(self, url):
        response = requests.put(
            f'{url}/user/{self.user_id}/update', json=self.payload_update)
        assert response.status_code == 200
        response_after = requests.get(
            f'{url}/user/id/{self.user_id}?full=true')
        user = response_after.json()['user']
        assert user['username'] == self.payload_update['username']
        assert user['name'] == self.payload_update['name']
        assert user['away'] == self.payload_update['away']
