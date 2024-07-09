import requests
import allure
import json
import requests
import pytest
from data.url_data import TestUrlData

from conftest import user_registration_and_delete
from data.auth_data import TestAuthData


@allure.feature('Тестируем функционал изменения данных пользователя')
class TestChangingUserData:
    @allure.title('Тестируем функционал изменения данных пользователя с авторизацией')
    def test_changing_user_data_with_registration(self):
        response = requests.post(f'{TestUrlData.URL}{TestUrlData.PATH_REG}', data=TestAuthData.dat)
        token = response.json()['accessToken']
        headers = {'Authorization': f'{token}'}
        response = requests.get(f'{TestUrlData.URL}{TestUrlData.PATH_USER}', headers=headers)
        assert response.status_code == 200
        requests.delete(f'{TestUrlData.URL}{TestUrlData.PATH_USER}', headers=headers)

    @allure.title('Тестируем функционал изменения данных пользователя без авторизации')
    def test_changing_user_data_without_registration(self):
        headers = {'Authorization': f'{TestAuthData.token}'}
        response = requests.get(f'{TestUrlData.URL}{TestUrlData.PATH_USER}', headers=headers)
        assert response.status_code == 401
