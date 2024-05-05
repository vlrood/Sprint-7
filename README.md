# Sprint-7
Автоматизировано API Яндекс.Самоката:

**helper:**

Созданы вспомогательные методы

modify_create_login_body - изменение тела запроса на логин курьера в системе.
modify_create_order_body - изменение тела запроса на создание заказа.

**scooter_api:**

create_courier - ручка создания курьера.

login_courier - ручка логина курьера в системе.

create_order - ручка создания заказа.
get_order_list - ручка получения списка заказа.

**conftest:**

default_courier - фикстура, передающая рандомные тестовые данные.
create_and_delete_courier - фикстура принимающая и удалающая рандомные тестовые данные.

**_test_creating_a_courier:_**

test_create_courier_create_and_delete_courier_success - проверка создания курьера. Ождается статус ответа 201.
test_create_courier_without_password_or_login_default_courier_arg_shows_error - проверка создания курьера без логина
или пароля. Использована параметризация. Ожидается статус ответа 400.
test_create_identical_login_courier_create_and_delete_courier_shows_error - проверка создания двух одинаковых курьеров.
Ожидается статус ответа 409.

**_test_login_courier:_**
test_courier_login_create_and_delete_courier_should_be_authorized - проверка запроса на логин курьера в системе.
Статус ответе - 200. Тело ответа содержит id курьера
test_request_without_login_shows_error - проверка запроса с неуказанным логином курьера. Статус ответа - 400
test_request_without_password_shows_error - проверка запроса с неуказанным паролем курьера. Статус ответа - 
400 
test_authorization_under_non_existent_user_shows_error - проверка запроса с несуществующим курьером. Ответ 404.

**test_order:**
test_create_order_color_should_be_created - проверка запроса на создание заказа. Использована параметризация.
Ответ - 201, в теле ответа трэк для отслеживания заказа

test_get_order_list_should_display_order_list - проверка запроса на получение списка заказов. Статус ответа - 200,
в теле ответа список, состоящий из заказов.

В файл data вынесены тестовые данные.
Сгенерированы Allure-отчёты в allure_results.







