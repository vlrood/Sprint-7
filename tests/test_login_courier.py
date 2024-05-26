import allure
import pytest

from data import CourierError
import helper
from scooter_api import CourierApi


class TestLoginCourier:
    @allure.title('Проверка получения в ответе id курьера')
    @allure.description('Создание курьера, изменение тела запроса, проверка статуса и тела ответа')
    def test_courier_login_create_and_delete_courier_should_be_authorized(self, create_and_delete_courier):
        CourierApi.create_courier(create_and_delete_courier)
        del create_and_delete_courier['firstName']
        login_request = CourierApi.login_courier(create_and_delete_courier)
        courier_id = login_request.json()['id']

        assert login_request.status_code == 200 and courier_id is not None and courier_id > 0

    @allure.title('Проверка ошибки запроса без логина')
    @allure.description('Присваиваем пустое значение логину, проверяем статус и тело ответа')
    def test_request_without_login_shows_error(self):
        body = helper.ChangeTestDataHelper.modify_create_login_body('login', '')
        login_response = CourierApi.login_courier(body)

        assert (login_response.status_code == 400 and
                login_response.json()['message'] == CourierError.LOGIN_REQUEST_WITHOUT_DATA)

    @allure.title('Проверка ошибки запроса без пароля')
    @allure.description('Присваиваем пустое значение паролю, проверяем статус и тело ответа')
    def test_request_without_password_shows_error(self):
        body = helper.ChangeTestDataHelper.modify_create_login_body('password', '')
        login_response = CourierApi.login_courier(body)

        assert (login_response.status_code == 400 and
                login_response.json()['message'] == CourierError.LOGIN_REQUEST_WITHOUT_DATA)

    @allure.title('Проверка ошибки запроса с несуществующим курьером')
    @allure.description('Изменяем логин, проверяем статус и тело ответа')
    def test_authorization_under_non_existent_user_shows_error(self):
        body = helper.ChangeTestDataHelper.modify_create_login_body('login', 'yves')
        login_response = CourierApi.login_courier(body)

        assert (login_response.status_code == 404 and
                login_response.json()['message'] == CourierError.LOGIN_REQUEST_WITH_NONEXISTENT_COURIER)
