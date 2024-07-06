import requests
import allure
from data.auth_data import TestAuthData


@allure.title('Тестируем функционал получение заказов конкретного пользователя')
class TestReceivingOrdersFromUser:
    @allure.title('Тестируем функционал создания заказа авторизировнным пользователем')
    def test_receiving_orders_from_authorized_user(self):
        response = requests.post('https://stellarburgers.nomoreparties.site/api/auth/register', data=TestAuthData.dat)
        token = response.json()['accessToken']
        headers = {'Authorization': f'{token}'}
        response = requests.get('https://stellarburgers.nomoreparties.site/api/orders', headers=headers)
        assert response.status_code == 200
        requests.delete('https://stellarburgers.nomoreparties.site/api/auth/user', headers=headers)

    @allure.title('Тестируем функционал создания заказа не авторизировнным пользователем')
    def test_receiving_orders_from_not_authorized_user(self):
        headers = {'Authorization': f'{TestAuthData.token}'}
        response = requests.get('https://stellarburgers.nomoreparties.site/api/orders', headers=headers)
        assert response.status_code == 401
