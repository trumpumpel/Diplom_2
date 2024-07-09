import requests
import allure
import json
import requests
import pytest
from data.url_data import TestUrlData
from conftest import user_registration_and_delete
from data.auth_data import TestAuthData


@allure.feature('Тестируем функционал создания заказа')
class TestCreatingAnOrder:
    @allure.title('Тестируем функционал создания заказа с авторизацией')
    def test_creating_order_with_authorization(self, user_registration_and_delete):
        response = requests.post(f'{TestUrlData.URL}{TestUrlData.PATH_ORDERS}', data=TestAuthData.order)
        assert response.status_code == 200

    @allure.title('Тестируем функционал создания заказа без авторизации')
    def test_creating_order_without_authorization(self):
        response = requests.post(f'{TestUrlData.URL}{TestUrlData.PATH_ORDERS}', data=TestAuthData.order)
        assert response.status_code == 200

    @allure.title('Тестируем функционал создания заказа с ингридиентами')
    def test_creating_order_with_ingredients(self):
        response = requests.post(f'{TestUrlData.URL}{TestUrlData.PATH_ORDERS}', data=TestAuthData.order)
        assert response.status_code == 200

    @allure.title('Тестируем функционал создания заказа без ингридиентов')
    def test_creating_order_without_ingredients(self):
        response = requests.post(f'{TestUrlData.URL}{TestUrlData.PATH_ORDERS}', data=TestAuthData.order1)
        assert response.status_code == 400

    @allure.title('Тестируем функционал создания заказа с неверным хешем ингредиентов')
    def test_creating_order_with_incorrect_hash_of_ingredients(self):
        response = requests.post(f'{TestUrlData.URL}{TestUrlData.PATH_ORDERS}', data=TestAuthData.order2)
        assert response.status_code == 400
