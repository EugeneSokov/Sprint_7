import pytest
import allure
import requests
import json


url = 'https://qa-scooter.praktikum-services.ru/api/v1'
id=230613
class TestListOrder:

    @allure.title(        'Проверка ручки списка заказов для существующего id курьера')
    @allure.description('Сравниваем ожидаемый статус-код ответа "200" с фактическим')
    def test_list_of_order_existing_id(self):
        courierID = {"courierId": {id}}
        r_list_orders = requests. get(f"{url}/orders", params = courierID)
        assert r_list_orders.status_code == 200
        assert ('orders' in json.loads(r_list_orders.text)) == True

    @allure.title(        'Проверка ручки списка заказов для несуществующего id курьера')
    @allure.description('Сравниваем ожидаемый статус-код ответа "404" с фактическим')
    def test_list_of_order_not_existing_id(self):
            id_false=500
            courierID = {"courierId": id_false}
            r_list_orders = requests.get(f"{url}/orders", params=courierID)
            assert r_list_orders.status_code == 404
            assert r_list_orders.json()["message"] == f"Курьер с идентификатором {id_false} не найден"