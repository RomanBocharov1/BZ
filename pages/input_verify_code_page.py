import time
from tests.conftest import driver
from pages.auth_input_number_page import data_for_test, system_numbersKeys

# Экран ввода кода при авторизации через телефон


class InputVerifyCodePage:

    @staticmethod
    def input_verify_code():  # ввод кода из смс
        time.sleep(1)
        for i in range(len(data_for_test["auth_code"])):
            number_from_phone = data_for_test["auth_code"][i]
            keyboard_code = system_numbersKeys[number_from_phone]
            driver.press_keycode(keyboard_code)


