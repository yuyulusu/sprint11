import requests
import unittest
from configuration import API_URl, ORDER_ENDPOINT, TRACK_ENDPOINT
from data import order_data

def test_create_and_get_order(self):
  
        # Выполнить запрос на создание заказа
        create_response = requests.post(f"{self.API_URL}ORDER_ENDPOINT", json=order_data)
        self.assertEqual(create_response.status_code, 201, "Order creation failed")
        
        # Сохранить номер трека заказа
        track_number = create_response.json().get("track")
        self.assertIsNotNone(track_number, "Track number is missing")

        # Выполнить запрос на получение заказа по треку заказа
        get_response = requests.get(f"{self.API_URL}TRACK_ENDPOINT", params={"t": track_number})
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
