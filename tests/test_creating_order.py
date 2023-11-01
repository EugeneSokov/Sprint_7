import pytest
import allure
import requests
import json

url = 'https://qa-scooter.praktikum-services.ru/api/v1'
class TestCreateOrder:

    @allure.title(        'Проверка ручки создания заказа для самоката цветов "GREY" и "BLACK"')
    @allure.description('Сравниваем ожидаемый статус-код ответа "201" с фактическим')
    @pytest.mark.parametrize('color',["GREY", "BLACK",["GREY", "BLACK"],""])
    def test_creating_order(self, color):
        payload = {
            "firstName": "Lucio",
            "lastName": "Schubert",
            "address": "Mounting road, 149 apt.",
            "metroStation": 2,
            "phone": "+7 800 321 56 78",
            "rentTime": 4,
            "deliveryDate": "2023-09-15",
            "comment": "Run, courier, run",
            "color": color
                           }
        payload_string = json.dumps(payload)
        r_order = requests.post(f"{url}/orders", data=payload_string)
        track_number = r_order.json()["track"]
        data_track = {"track": {track_number}}
        assert r_order.status_code == 201
        assert ('track' in json.loads(r_order.text)) == True
        r_order_cancel = requests.put(f"{url}/orders/cancel", params=data_track)