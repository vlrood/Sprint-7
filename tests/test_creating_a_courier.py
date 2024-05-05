import allure
import pytest
from scooter_api import CourierApi
from data import CourierError


class TestCreatingCourier:
    @allure.title('Проверка успешности создания курьера')
    @allure.description('Отправка запроса на создание курьера, проверка статуса и тела ответа')
    def test_create_courier_create_and_delete_courier_success(self, create_and_delete_courier):
        courier_request = CourierApi.create_courier(create_and_delete_courier)

        assert courier_request.status_code == 201 and courier_request.json()['ok'] is True

    @allure.title('Проверка невозможности создания курьера при отсутствии обязательных полей')
    @allure.description('Отправка запроса без логина и пароля, проверка статуса и тела ответа')
    @pytest.mark.parametrize('arg', ['login', 'password'])
    def test_create_courier_without_password_or_login_default_courier_arg_shows_error(self, default_courier, arg):
        del default_courier[arg]
        created_courier_request = CourierApi.create_courier(default_courier)

        assert (created_courier_request.status_code == 400
                and created_courier_request.json()['message'] == CourierError.REQUEST_WITHOUT_PASSWORD_OR_LOGIN)

    @allure.title('Проверка ошибки создания курьеров с индетичным логином')
    @allure.description('Отправка двух запросов на создание курьера, проверка статуса и тела ответа')
    def test_create_identical_login_courier_create_and_delete_courier_shows_error(self, create_and_delete_courier):
        CourierApi.create_courier(create_and_delete_courier)
        courier_request_2 = CourierApi.create_courier(create_and_delete_courier)

        assert (courier_request_2.status_code == 409 and
                courier_request_2.json()['message'] == CourierError.REQUEST_WITH_IDENTICAL_LOGIN)
