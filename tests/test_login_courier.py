import pytest
import allure
import requests
import json


url = 'https://qa-scooter.praktikum-services.ru/api/v1'
login = "vorona"
password = "987654321qwerasdzxc"
class TestLoginCourier:

    @allure.title(        'Проверка ручки логина курьера с существующим набором (login, password)')
    @allure.description('Сравниваем ожидаемый статус-код ответа "200" с фактическим')
    def test_loginning_courier_check(self):
        login_data = {
           "login": login,
           "password": password
                  }

        r_login = requests.post(f"{url}/courier/login", data=login_data)
        id=r_login.json()["id"]
        assert r_login.status_code == 200
        assert ('id' in json.loads(r_login.text)) == True

    @allure.title(        'Проверка ручки логина курьера с пустым полем для логина')
    @allure.description('Сравниваем ожидаемый статус-код ответа "400" с фактическим')
    def test_loginning_courier_empty_login_field(self):
        login_data = {
           "password": password
                  }
        r_login = requests.post(f"{url}/courier/login", data=login_data)

        assert r_login.status_code == 400
        assert r_login.json()["message"] == "Недостаточно данных для входа"

    @allure.title(        'Проверка ручки логина курьера с несуществующим логином')
    @allure.description('Сравниваем ожидаемый статус-код ответа "404" с фактическим')
    def test_loginning_courier_false_login(self):
        login_data = {
            "login": "vorona soroka",
            "password": password
                }
        r_login = requests.post(f"{url}/courier/login", data=login_data)

        assert r_login.status_code == 404
        assert r_login.json()["message"] == "Учетная запись не найдена"

    @allure.title(        'Проверка ручки логина курьера с неверным паролем')
    @allure.description('Сравниваем ожидаемый статус-код ответа "404" с фактическим')
    def test_loginning_courier_false_password(self):
        login_data = {
              "login":login,
              "password": "12345678"
                   }
        r_login = requests.post(f"{url}/courier/login", data=login_data)

        assert r_login.status_code == 404
        assert r_login.json()["message"] == "Учетная запись не найдена"

    @allure.title(        'Проверка ручки логина курьера с пустым полем для пароля')
    @allure.description('Сравниваем ожидаемый статус-код ответа "400" с фактическим')
    def test_loginning_courier_empty_passw_field(self):
        login_data = {
           "login": login
            }

        r_login = requests.post(f"{url}/courier/login", data=login_data)

        assert r_login.status_code == 400
        assert r.json()["message"] == "Недостаточно данных для входа"
