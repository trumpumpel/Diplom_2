import allure
import pytest
import requests
from data.url_data import TestUrlData
from data.auth_data import TestAuthData


@allure.feature('Тестируем функционал изменения данных пользователя')
class TestChangingUserData:
    @allure.title('Тестируем функционал изменения данных пользователя с авторизацией')
    def test_changing_user_data_with_registration(self, user_registration_and_delete):
        response = requests.get(f'{TestUrlData.URL}{TestUrlData.PATH_USER}', headers=self.headers)
        assert '"success":true' in response.text

    @allure.title('Тестируем функционал изменения данных пользователя без авторизации')
    def test_changing_user_data_without_registration(self):
        headers = {'Authorization': f'{TestAuthData.token}'}
        response = requests.get(f'{TestUrlData.URL}{TestUrlData.PATH_USER}', headers=headers)
        assert '"success":false' in response.text
