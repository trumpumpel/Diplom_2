import requests
import allure
import requests
from conftest import user_registration_and_delete
from data.auth_data import TestAuthData


@allure.title('Тестируем функционал создания пользователя')
class TestCreatingUser:
    @allure.title('Тестируем создание уникального пользователя')
    def test_register_courier(self):
        response = requests.post('https://stellarburgers.nomoreparties.site/api/auth/register', data=TestAuthData.dat)
        token = response.json()['accessToken']
        headers = {'Authorization': f'{token}'}
        response = requests.delete('https://stellarburgers.nomoreparties.site/api/auth/user', headers=headers)
        assert response.status_code == 202

    @allure.title('Тестируем создание пользователя, который уже зарегистрирован')
    def test_register_clone_courier(self, user_registration_and_delete):
        response = requests.post('https://stellarburgers.nomoreparties.site/api/auth/register', data=TestAuthData.dat)
        assert response.status_code == 403

    @allure.title('Тестируем создание пользователя, который не заполнил поле email')
    def test_register_courier_without_email(self):
        response = requests.post('https://stellarburgers.nomoreparties.site/api/auth/register', data=TestAuthData.dat1)
        assert response.status_code == 403

    @allure.title('Тестируем создание пользователя, который не заполнил поле пароль')
    def test_register_courier_without_password(self):
        response = requests.post('https://stellarburgers.nomoreparties.site/api/auth/register', data=TestAuthData.dat2)
        assert response.status_code == 403

    @allure.title('Тестируем создание пользователя, который не заполнил поле имя')
    def test_register_courier_without_name(self):
        response = requests.post('https://stellarburgers.nomoreparties.site/api/auth/register', data=TestAuthData.dat3)
        assert response.status_code == 403
