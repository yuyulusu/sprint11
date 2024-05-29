import requests
import unittest
import pytest
#from configuration import API_URl, ORDER_ENDPOINT, TRACK_ENDPOINT
#from data import order_data
API_URL = 'https://f9b63350-120a-4f97-ae40-babd83ae54bf.serverhub.praktikum-services.ru'
ORDER_ENDPOINT = '/api/v1/orders'
TRACK_ENDPOINT = '/api/v1/orders/track'
order_data = {
  "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        "BLACK"
    ]
}
class TestOrderGet(unittest.TestCase):
        API_URL = 'https://f9b63350-120a-4f97-ae40-babd83ae54bf.serverhub.praktikum-services.ru'

        def test_create_and_get_order(self):
  
                # Выполнить запрос на создание заказа
                print(API_URL+ORDER_ENDPOINT)
                create_response = requests.post(API_URL+ORDER_ENDPOINT, json=order_data)
                self.assertEqual(create_response.status_code, 201, "Order creation failed")
                
                # Сохранить номер трека заказа
                track_number = create_response.json().get("track")
                self.assertIsNotNone(track_number, "Track number is missing")
        
                # Выполнить запрос на получение заказа по треку заказа
                get_response = requests.get(API_URL+TRACK_ENDPOINT, params={"t": track_number})
                self.assertEqual(get_response.status_code, 200, "Failed to get order details")
        
                # Проверить содержимое ответа
                order = get_response.json().get("order")
                self.assertIsNotNone(order, "Order details are missing")
                self.assertEqual(order["firstName"], order_data["firstName"], "First name does not match")
                self.assertEqual(order["lastName"], order_data["lastName"], "Last name does not match")
                self.assertEqual(order["address"], order_data["address"], "Address does not match")
                self.assertEqual(order["phone"], order_data["phone"], "Phone number does not match")

if __name__ == "__main__":
    unittest.main()
    
