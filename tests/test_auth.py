import requests
from config import host


class TestUtiles:

    payload = {
        "login": "johndoe",
        "password": "1D1"
    }

    def test_sign_in_with_no_user(self):
        response = requests.post(f'{host}/auth/signin', json=self.payload)
        assert response.status_code == 200
        assert response.json()['status']

    def test_sign_up(self):
        response = requests.post(f'{host}/auth/signup', json=self.payload)
        assert response.status_code == 200

    def test_sign_in_with_user(self):
        response = requests.post(f'{host}/auth/signin', json=self.payload)
        assert response.status_code == 200
        assert response.json()['access_token']
