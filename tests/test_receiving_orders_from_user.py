import requests
import allure
from data.auth_data import TestAuthData
from data.url_data import TestUrlData


@allure.title('Тестируем функционал получение заказов конкретного пользователя')
class TestReceivingOrdersFromUser:
    @allure.title('Тестируем функционал создания заказа авторизировнным пользователем')
    def test_receiving_orders_from_authorized_user(self):
        response = requests.post(f'{TestUrlData.URL}{TestUrlData.PATH_REG}', data=TestAuthData.dat)
        token = response.json()['accessToken']
        headers = {'Authorization': f'{token}'}
        response = requests.get(f'{TestUrlData.URL}{TestUrlData.PATH_ORDERS}', headers=headers)
        assert response.status_code == 200
        requests.delete(f'{TestUrlData.URL}{TestUrlData.PATH_USER}', headers=headers)

    @allure.title('Тестируем функционал создания заказа не авторизировнным пользователем')
    def test_receiving_orders_from_not_authorized_user(self):
        headers = {'Authorization': f'{TestAuthData.token}'}
        response = requests.get(f'{TestUrlData.URL}{TestUrlData.PATH_ORDERS}', headers=headers)
        assert response.status_code == 401
