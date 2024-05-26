import random
import allure
import pytest
import requests
from faker import Faker
import urls


@allure.step('Формируем тело для создания курьера')
@pytest.fixture()
def default_courier():
    fake = Faker()
    payload = {
        'login': fake.user_name(),
        'password': random.randint(10000, 9999999999),
        'firstName': fake.first_name()

    }

    return payload


@allure.step('Удаление тестовых данных')
@pytest.fixture()
def create_and_delete_courier(default_courier):
    yield default_courier

    response = requests.post(f'{urls.BASE_URL}/{urls.LOGIN_COURIER_PATH}',
                             data={'login': default_courier['login'], 'password': default_courier['password']})
    response_json = response.json()["id"]
    requests.delete(f'{urls.BASE_URL}/{urls.DELETE_COURIER_PATH}/{response_json}')
