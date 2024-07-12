import requests
import pytest
from data.url_data import TestUrlData
from data.auth_data import TestAuthData


@pytest.fixture()
def user_registration_and_delete(request):
    response = requests.post(f'{TestUrlData.URL}{TestUrlData.PATH_REG}', data=TestAuthData.dat)
    request.cls.token = response.json()['accessToken']
    request.cls.headers = {'Authorization': f'{request.cls.token}'}
    yield
    requests.delete(f'{TestUrlData.URL}{TestUrlData.PATH_USER}', headers=request.cls.headers)
