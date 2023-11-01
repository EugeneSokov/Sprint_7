import pytest
import allure
import requests
import json
from faker import Faker


fake = Faker()
url = 'https://qa-scooter.praktikum-services.ru/api/v1'
class TestCreatingCourier:
    @allure.title(        'Проверка ручки создания курьера')
    @allure.description('Сравниваем ожидаемый статус-код ответа "201" с фактическим')
    def test_creating_courier_unical_check_status_code(self):
        log = fake.name()
        passw = fake.password()
        first_name = fake.first_name()
        payload = {
           "login": log,
           "password": passw,
           "firstName": first_name
                  }
        r = requests.post(f"{url}/courier", data=payload)

        assert r.status_code == 201
        assert r.json()["ok"] == True

        r_log = requests.post(f"{url}/courier/login", data={"login": log, "password": passw})
        id=r_log.json()["id"]
        r_delete = requests.delete(f"{url}/courier/{id}")

    @allure.title(        'Проверка ручки создания курьера с пустым полем для пароля')
    @allure.description('Сравниваем ожидаемый статус-код ответа "400" с фактическим')
    def test_creating_courier_unical_empty_some_field(self):
            log = fake.name()
            first_name = fake.first_name()
            payload = {
                "login": log,
                "firstName": first_name
            }
            r = requests.post(f"{url}/courier", data=payload)

            assert r.status_code == 400
            assert r.json()["message"] == "Недостаточно данных для создания учетной записи"

    @allure.title(        'Проверка ручки создания курьера с существующими параметрами (login, password)')
    @allure.description('Сравниваем ожидаемый статус-код ответа "409" с фактическим')
    def test_creating_courier_duplicate(self):
            payload = {
                "login": "vorona",
                "password": "987654321qwerasdzxc",
                "firstName": "voronickhina"
            }
            r = requests.post(f"{url}/courier", data=payload)

            assert r.status_code  == 409
            assert r.json()["message"] == "Этот логин уже используется."

    @allure.title(        'Проверка ручки создания курьера с повторяющимся логином существующего курьера')
    @allure.description('Сравниваем ожидаемый статус-код ответа "409" с фактическим')
    def test_creating_courier_duplicate_login(self):
                passw = fake.password()
                first_name = fake.first_name()
                payload = {
                    "login": "vorona",
                    "password": passw,
                    "firstName": first_name
                }
                r = requests.post(f"{url}/courier", data=payload)

                assert r.status_code == 409
                assert r.json()["message"] == "Этот логин уже используется."
