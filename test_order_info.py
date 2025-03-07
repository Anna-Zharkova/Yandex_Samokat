# Анна Жаркова, 27-я когорта — Финальный проект. Инженер по тестированию плюс

import configuration
import requests
import data
import sender_stand_request

# Создать заказ
def create_new_order(body):
    return requests.post (configuration.URL_SERVICE + configuration.URL_ORDER_CREATE,
                          json=body)
response = create_new_order(data.order_body)
print(response.status_code)
print(response.json())

# Получить трек заказа
def get_order(track):
    return requests.get (configuration.URL_SERVICE + configuration.URL_ORDER_TRACK + str(track))

# Получить данные заказа
def track_code():
    response_create_order = create_new_order(data.order_body)
    track = response_create_order.json()["track"]
    return get_order(track).status_code

def test_get_order_by_track():
    assert track_code() == 200