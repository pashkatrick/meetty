import requests
from config import host
import pytest


class TestAvailablity:

    payload = {
        "slots": [
            {
                "day": 6,
                "time_from": 540,
                "time_to": 630
            },
            {
                "day": 7,
                "time_from": 540,
                "time_to": 1020
            }
        ]
    }

    '''
    Free Time Slots
    '''

    def test_get_user_free_time_frames(self):
        response = requests.get(f'{host}/user/5/free')
        assert response.status_code == 200
        assert len(response.json()['free_slots']) >= 3

    def test_add_free_time_frames(self):
        response = requests.post(f'{host}/user/6/free/add', json=self.payload)
        assert response.status_code == 200
        assert response.json()['status'] == 'data was added'

    def test_add_free_time_duplicates(self):
        response = requests.post(f'{host}/user/8/free/add', json=self.payload)
        assert response.status_code == 200
        # assert response.json()['status'] == 'duplicate or internal error'

    '''
    Busy Time Slots
    '''

    def test_get_user_busy_time_frames(self):
        response = requests.get(f'{host}/user/7/busy')
        assert response.status_code == 200
        assert len(response.json()['busy_slots']) >= 3

    def test_add_busy_time_frames(self):
        response = requests.post(f'{host}/user/2/busy/add', json=self.payload)
        assert response.status_code == 200
        # assert response.json()['status'] == 'data was added'

    def test_add_busy_time_duplicates(self):
        response = requests.post(f'{host}/user/9/busy/add', json=self.payload)
        assert response.status_code == 200
        # assert response.json()['status'] == 'duplicate or internal error'