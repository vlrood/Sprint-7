import data


class ChangeTestDataHelper:
    @staticmethod
    def modify_create_login_body(key, value):
        body = data.TestDataCreateCourier.LOGIN_PAYLOAD.copy()
        body[key] = value

        return body

    @staticmethod
    def modify_create_order_body(key, value):
        body = data.TestDataCreateOrder.ORDER_PAYLOAD.copy()
        body[key] = value

        return body
