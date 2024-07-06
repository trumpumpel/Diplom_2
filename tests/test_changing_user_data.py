import requests
import allure
import json
import requests
import pytest
from conftest import user_registration_and_delete
from data.auth_data import TestAuthData


@allure.title('Тестируем функционал изменения данных пользователя')
class TestChangingUserData:
    @allure.title('Тестируем функционал изменения данных пользователя с авторизацией')
    def test_changing_user_data_with_registration(self):
        response = requests.post('https://stellarburgers.nomoreparties.site/api/auth/register', data=TestAuthData.dat)
        token = response.json()['accessToken']
        headers = {'Authorization': f'{token}'}
        response = requests.get('https://stellarburgers.nomoreparties.site/api/auth/user', headers=headers)
        assert response.status_code == 200
        requests.delete('https://stellarburgers.nomoreparties.site/api/auth/user', headers=headers)

    @allure.title('Тестируем функционал изменения данных пользователя без авторизации')
    def test_changing_user_data_without_registration(self):
        headers = {'Authorization': f'{TestAuthData.token}'}
        response = requests.get('https://stellarburgers.nomoreparties.site/api/auth/user', headers=headers)
        assert response.status_code == 401
