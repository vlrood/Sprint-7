
class TestDataCreateOrder:
    ORDER_PAYLOAD = {
        'firstName': 'Ninja',
        'lastName': 'Uzumaki',
        'address': 'Konoha, 142 apt.',
        'metroStation': 4,
        'phone': '+7 800 355 35 35',
        'rentTime': 5,
        'deliveryDate': "2024-05-08",
        'comment': 'Saske, come back to Konoha',
        'color': [
            'BLACK'
        ]
    }


class TestDataCreateCourier:
    LOGIN_PAYLOAD = {
            'login': 'saint',
            'password': '1234567',
        }


class CourierError:
    REQUEST_WITHOUT_PASSWORD_OR_LOGIN = 'Недостаточно данных для создания учетной записи'
    REQUEST_WITH_IDENTICAL_LOGIN = 'Этот логин уже используется. Попробуйте другой.'
    LOGIN_REQUEST_WITHOUT_DATA = 'Недостаточно данных для входа'
    LOGIN_REQUEST_WITH_NONEXISTENT_COURIER = 'Учетная запись не найдена'
