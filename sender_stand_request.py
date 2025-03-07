# Анна Жаркова, 27-я когорта — Финальный проект. Инженер по тестированию плюс

import configuration
import requests
import data

# Создать заказ
def create_new_order(body):
    return requests.post (configuration.URL_SERVICE + configuration.URL_ORDER_CREATE,
                          json=body)
response = create_new_order(data.order_body)
print(response.status_code)
print(response.json())

# Получить трека заказа
def get_order(track):
    return requests.get (configuration.URL_SERVICE + configuration.URL_ORDER_TRACK + str(track))