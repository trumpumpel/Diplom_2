import requests
import pytest
from data.url_data import TestUrlData
from data.auth_data import TestAuthData


@pytest.fixture
def user_registration_and_delete():
    response = requests.post(f'{TestUrlData.URL}{TestUrlData.PATH_REG}', data=TestAuthData.dat)
    token = response.json()['accessToken']
    headers = {'Authorization': f'{token}'}
    yield
    requests.delete(f'{TestUrlData.URL}{TestUrlData.PATH_USER}', headers=headers)
