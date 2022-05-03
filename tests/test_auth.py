import requests
from config import host
from random import randint
import pytest


@pytest.mark.skip('no valid data')
class TestUtiles():

    login = f'johndoe-{randint(0, 100)}'
    payload = {
        'login': login,
        'password': '1D1'
    }

    def test_sign_in_with_no_user(self):
        response = requests.post(f'{host}/auth/signin', json=self.payload)
        assert response.status_code == 200
        assert response.json()['data'] == 'user doesn\'t exist'

    def test_sign_up(self):
        response = requests.post(f'{host}/auth/signup', json=self.payload)
        assert response.status_code == 200
        assert response.json()['status'] == f'user {self.login} was registered'

    def test_sign_in_with_user(self):
        response = requests.post(f'{host}/auth/signin', json=self.payload)
        assert response.status_code == 200
        assert response.json()['token']
        pytest.access_token = response.json()['token']

    def test_access_token(self):
        response = requests.get(
            f'{host}/ready', headers={'Authorization': f'Bearer {pytest.access_token}'})
        assert response.json()['status'] == f'ok, {self.login}'
