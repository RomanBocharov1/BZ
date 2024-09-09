import logging
import requests


class PowerBankReturnerApiClient:
    def __init__(self, returner_url, username, password):
        self.returner_url = returner_url
        self.username = username
        self.password = password
        self.session = requests.Session()

    def login(self):
        login_url = f'{self.returner_url}/login'
        login_data = {"username": self.username, "password": self.password}
        response = self.session.post(login_url, data=login_data)
        if response.ok:
            logging.info("Login successful.")
            return True
        else:
            logging.error(f"Login failed. Status code: {response.status_code}. Response: {response.text}")
            return False

    def return_powerbank_relink(self, vending_number, serial_number):
        if self.login():
            finish_url = f'{self.returner_url}/finish?id={vending_number}&serial_number={serial_number}'
            response = self.session.get(finish_url)
            if response.ok:
                logging.info("Order finish successful.")
            else:
                logging.error(f"Failed to finish order. Status code: {response.status_code}. Response: {response.text}")
            return response
        else:
            return None


returner_pb = PowerBankReturnerApiClient(returner_url='https://stagerelink-returner.berizaryad.ru',
                                         username='b.munirovich@berizaryad.ru',
                                         password='qN7wwLEP'
                                         )
