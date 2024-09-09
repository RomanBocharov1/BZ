from selenium.webdriver.common.by import By
from tests.conftest import driver
import random

data_for_test = {"auth_code": "0001"}  # Данные для тестов

system_numbersKeys = {'0': '7',  # Данные для набора системных цифр на клавиатуре
                      '1': '8',
                      '2': '9',
                      '3': '10',
                      '4': '11',
                      '5': '12',
                      '6': '13',
                      '7': '14',
                      '8': '15',
                      '9': '16'}


class AuthInputNumberPage:  # Экран ввода номера телефона при авторизации

    @staticmethod
    def tap_code_country(resource_id='ru.berizaryad.android.staging:id/text_input_country_prefix'):
        driver.find_element(By.ID, resource_id).click()  # Тап на код страны

    @staticmethod
    def input_num_phone():  # ввод номера телефона
        def generate_random_number():
            num_list = []
            while len(num_list) < 9:
                num = str(random.randint(0, 9))
                if not num in num_list:
                    num_list.append(num)
            str_join = ''.join(num_list)
            random_number = '9' + str_join
            return random_number
        driver.find_element(By.ID, 'ru.berizaryad.android.staging:id/edPhone').click()
        for i in range(len(generate_random_number())):
            number_from_phone = generate_random_number()[i]
            keyboard_code = system_numbersKeys[number_from_phone]
            driver.press_keycode(keyboard_code)

    @staticmethod
    def tap_button_next(resource_id='ru.berizaryad.android.staging:id/btnNext'):  # тап на кнопку "Далее"
        driver.find_element(By.ID, resource_id).click()




