import allure
import requests
from data.url_data import TestUrlData
from data.auth_data import TestAuthData


@allure.feature('Тестируем функционал изменения данных пользователя')
class TestChangingUserData:
    @allure.title('Тестируем функционал изменения данных пользователя с авторизацией')
    def test_changing_user_data_with_registration(self):
        response = requests.post(f'{TestUrlData.URL}{TestUrlData.PATH_REG}', data=TestAuthData.dat)
        token = response.json()['accessToken']
        headers = {'Authorization': f'{token}'}
        response = requests.get(f'{TestUrlData.URL}{TestUrlData.PATH_USER}', headers=headers)
        assert '"success":true' in response.text
        requests.delete(f'{TestUrlData.URL}{TestUrlData.PATH_USER}', headers=headers)

    @allure.title('Тестируем функционал изменения данных пользователя без авторизации')
    def test_changing_user_data_without_registration(self):
        headers = {'Authorization': f'{TestAuthData.token}'}
        response = requests.get(f'{TestUrlData.URL}{TestUrlData.PATH_USER}', headers=headers)
        assert '"success":false' in response.text
