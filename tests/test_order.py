import allure
import pytest
import helper
from scooter_api import OrderApi


class TestOrder:
    @allure.title('Проверка создания заказа')
    @allure.description('Отправляем четыре запроса с разными цветами, проверяем статус и тело ответа')
    @pytest.mark.parametrize('color', [
        pytest.param(['BLACK']),
        pytest.param(['GREY']),
        pytest.param([]),
        pytest.param(['BLACK', 'GREY'])
    ])
    def test_create_order_color_should_be_created(self, color):
        body = helper.ChangeTestDataHelper.modify_create_order_body('color', color)
        order_response = OrderApi.create_order(body)

        assert order_response.status_code == 201 and order_response.json()['track'] is not None


class TestOrderList:
    @allure.title('Проверка возвращения в ответе списка заказов')
    def test_get_order_list_should_display_order_list(self):
        order_list_response = OrderApi.get_order_list()

        assert order_list_response.status_code == 200 and order_list_response.json()['orders'] is not None
