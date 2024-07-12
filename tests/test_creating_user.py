import allure
import requests
from data.auth_data import TestAuthData
from data.url_data import TestUrlData


@allure.feature('Тестируем функционал создания пользователя')
class TestCreatingUser:
    @allure.title('Тестируем создание уникального пользователя')
    def test_register_courier(self, user_registration_and_delete):
        response = requests.delete(f'{TestUrlData.URL}{TestUrlData.PATH_USER}', headers=self.headers)
        assert '{"success":true,"message":"User successfully removed"}' == response.text

    @allure.title('Тестируем создание пользователя, который уже зарегистрирован')
    def test_register_clone_courier(self, user_registration_and_delete):
        response = requests.post(f'{TestUrlData.URL}{TestUrlData.PATH_REG}', data=TestAuthData.dat)
        assert '{"success":false,"message":"User already exists"}' == response.text

    @allure.title('Тестируем создание пользователя, который не заполнил поле email')
    def test_register_courier_without_email(self):
        response = requests.post(f'{TestUrlData.URL}{TestUrlData.PATH_REG}', data=TestAuthData.dat1)
        assert '{"success":false,"message":"Email, password and name are required fields"}' == response.text

    @allure.title('Тестируем создание пользователя, который не заполнил поле пароль')
    def test_register_courier_without_password(self):
        response = requests.post(f'{TestUrlData.URL}{TestUrlData.PATH_REG}', data=TestAuthData.dat2)
        assert '{"success":false,"message":"Email, password and name are required fields"}' == response.text

    @allure.title('Тестируем создание пользователя, который не заполнил поле имя')
    def test_register_courier_without_name(self):
        response = requests.post(f'{TestUrlData.URL}{TestUrlData.PATH_REG}', data=TestAuthData.dat3)
        assert '{"success":false,"message":"Email, password and name are required fields"}' == response.text
