import allure
import requests
import urls


class CourierApi:

    @staticmethod
    @allure.step('Отправка запроса на создание курьера')
    def create_courier(body):
        return requests.post(f'{urls.BASE_URL}/{urls.CREATE_COURIER_PATH}', data=body)

    @staticmethod
    @allure.step('Отправка запроса на логин курьера в системе')
    def login_courier(body):
        return requests.post(f'{urls.BASE_URL}/{urls.LOGIN_COURIER_PATH}', data=body)


class OrderApi:

    @staticmethod
    @allure.step('Отправка запроса на создание заказа')
    def create_order(body):
        return requests.post(f'{urls.BASE_URL}/{urls.ORDER_PATH}', json=body)

    @staticmethod
    @allure.step('Отправка запроса на получение списка заказов')
    def get_order_list():
        return requests.get(f'{urls.BASE_URL}/{urls.ORDER_PATH}')
