from selenium.webdriver.common.by import By
from tests.conftest import driver

# Экран ввода номера аппарата


class InputNumVendingPage:

    number_vending = '11111'

    @staticmethod
    def permission_deny_btn():  # Тап на "Отклонить"
        driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_deny_button').click()

    @staticmethod
    def tap_next():  # Тап на кнопку "Далее"
        driver.find_element(By.ID, 'ru.berizaryad.android.staging:id/btnNextStep').click()

    @staticmethod
    def tap_support():  # Тап на "Поддержка"
        driver.find_element(By.ID, 'ru.berizaryad.android.staging:id/btn_support').click()

    @staticmethod
    def tap_cross():  # Тап на "Крестик"
        driver.find_element(By.ID, 'ru.berizaryad.android.staging:id/btn_close').click()

    @staticmethod
    def tap_scan_qr():  # Тап на "Сканировать QR"
        driver.find_element(By.ID, 'ru.berizaryad.android.staging:id/btnScanning').click()

    @staticmethod
    def send_keys_input_num_vending(number_or_keys=number_vending):  # Ввести номер куба
        btn = driver.find_element(By.ID, 'ru.berizaryad.android.staging:id/editTextNumber')
        btn.click()
        btn.clear()
        btn.send_keys(number_or_keys)

    @staticmethod
    def permission_allow_btn():  # Тап на "Разрешить"
        driver.find_element(By.ID,
                            'com.android.permissioncontroller:id/permission_allow_foreground_only_button').click()

