import requests
import allure
from data.auth_data import TestAuthData
from data.url_data import TestUrlData


@allure.feature('Тестируем функционал получение заказов конкретного пользователя')
class TestReceivingOrdersFromUser:
    @allure.title('Тестируем функционал создания заказа авторизировнным пользователем')
    def test_receiving_orders_from_authorized_user(self, user_registration_and_delete):
        response = requests.get(f'{TestUrlData.URL}{TestUrlData.PATH_ORDERS}', headers=self.headers)
        total = response.json()['total']
        totalToday = response.json()['totalToday']
        assert '{"success":true,"orders":[],"total":f'
        {total}
        ',"totalToday":f'
        {totalToday}
        '}' == response.text

    @allure.title('Тестируем функционал создания заказа не авторизировнным пользователем')
    def test_receiving_orders_from_not_authorized_user(self):
        response = requests.get(f'{TestUrlData.URL}{TestUrlData.PATH_ORDERS}', headers=TestAuthData.headers)
        assert '{"success":false,"message":"You should be authorised"}' == response.text
