import requests
import allure
from conftest import user_registration_and_delete
from data.auth_data import TestAuthData
from data.url_data import TestUrlData


@allure.feature('Тестируем функционал логина пользователя')
class TestLoginUser:
    @allure.title('Тестируем создание пользователя')
    def test_login_with_email_and_password(self, user_registration_and_delete):
        response = requests.post(f'{TestUrlData.URL}{TestUrlData.PATH_LOGIN}', data=TestAuthData.dat)
        assert response.status_code == 200

    @allure.title('Тестируем создание пользователя, который не заполнил поле email')
    def test_login_without_email(self, user_registration_and_delete):
        response = requests.post(f'{TestUrlData.URL}{TestUrlData.PATH_LOGIN}', data=TestAuthData.dat4)
        assert response.status_code == 401

    @allure.title('Тестируем создание пользователя, который не заполнил поле пароль')
    def test_login_without_password(self, user_registration_and_delete):
        response = requests.post(f'{TestUrlData.URL}{TestUrlData.PATH_LOGIN}', data=TestAuthData.dat5)
        assert response.status_code == 401

    @allure.title('Тестируем создание пользователя без регистрации')
    def test_login_without_registration(self):
        response = requests.post(f'{TestUrlData.URL}{TestUrlData.PATH_LOGIN}', data=TestAuthData.dat5)
        assert response.status_code == 401
