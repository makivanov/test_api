import requests
import allure
from jsonschema import validate
from core.cantracts import USER_DATA_SCHEME

BASE_URL = 'https://reqres.in'
LIST_USERS = '/api/users?page=2'
EMAIL_ENDS = 'reqres.in'


@allure.title('Проверка получения списка пользователей')
def test_list_users():
    with allure.step('Делаем запрос по адрессу ' + BASE_URL + LIST_USERS):
        response = requests.get(url= BASE_URL + LIST_USERS)
    with allure.step('Проверка кода ответа'):
        assert response.status_code == 200

    data = response.json()['data']
    for item in data:
        with allure.step('Проверка элемента из списка'):
            validate(item, USER_DATA_SCHEME)
            with allure.step('Проверка окончания email адреса'):
                assert item['email'].endswith(EMAIL_ENDS)