import requests
from config import host
import pytest


class TestUsers:

    def test_get_users(self):
        response = requests.get(
            f'{host}/users?limit=20&offset=1')
        assert response.status_code == 200
        assert len(response.json()['users'][0]) >= 10

    def test_get_user_by_id(self):
        response = requests.get(f'{host}/user/id/5')
        assert response.status_code == 200
        assert response.json()['user']

    def test_get_full_user(self):
        response = requests.get(f'{host}/user/id/6?full=true')
        users = response.json()['user']
        assert response.status_code == 200
        assert users
        pytest.test_username = users['username']
        pytest.test_name = users['name']

    def test_get_user_by_username(self):
        response = requests.get(f'{host}/{pytest.test_username}')
        assert response.json()['user'] == pytest.test_name

    # def test_add_user(self):
    #     pass

    # def test_update_user(self):
    #     pass
