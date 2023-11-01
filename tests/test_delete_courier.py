import pytest
import allure
import requests
import json
from faker import Faker


fake = Faker()
url = 'https://qa-scooter.praktikum-services.ru/api/v1'
class TestDeleteCourier:

    @allure.title(        'Проверка ручки удаления курьера с существующим id')
    @allure.description('Сравниваем ожидаемый статус-код ответа "200" с фактическим')
    def test_deletting_courier_existing_id(self):
        log = fake.name()
        passw = fake.password()
        first_name = fake.first_name()
        payload = {
           "login": log,
           "password": passw,
           "firstName": first_name
                  }
        r = requests.post(f"{url}/courier", data=payload)

        r_log = requests.post(f"{url}/courier/login", data={"login": log, "password": passw})
        id=r_log.json()["id"]
        r_delete = requests.delete(f"{url}/courier/{id}")

        assert r_delete.status_code == 200
        assert ('ok' in json.loads(r_delete.text)) == True

    @allure.title(        'Проверка ручки удаления курьера с несуществующим id')
    @allure.description('Сравниваем ожидаемый статус-код ответа "404" с фактическим')
    def test_deletting_courier_not_existing_id(self):

            id = 7
            r_delete = requests.delete(f"{url}/courier/{id}")

            assert r_delete.status_code == 404
            assert r_delete.json()["message"] == "Курьера с таким id нет"

    @allure.title(        'Проверка ручки удаления курьера без id')
    @allure.description('Сравниваем ожидаемый статус-код ответа "400" с фактическим')
    def test_deletting_courier_without_id(self):

            r_delete = requests.delete(f"{url}/courier/")

            assert r_delete.json()["message"] == "Недостаточно данных для удаления курьера"
            assert r_delete.status_code == 400
