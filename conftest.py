import requests
import pytest

from data.auth_data import TestAuthData


@pytest.fixture
def user_registration_and_delete():
    response = requests.post('https://stellarburgers.nomoreparties.site/api/auth/register', data=TestAuthData.dat)
    token = response.json()['accessToken']
    headers = {'Authorization': f'{token}'}
    yield
    requests.delete('https://stellarburgers.nomoreparties.site/api/auth/user', headers=headers)
