from selenium.webdriver.common.by import By
from tests.conftest import driver

# Экран скана куара


class ScanQrPage:

    @staticmethod
    def tap_permission_allow_btn():  # Тап на "Разрешить"
        driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()

    @staticmethod
    def btn_not_scan():  # Тап на кнопку "Не сканирует QR - код?"
        driver.find_element(By.ID, 'ru.berizaryad.android.staging:id/btnNotScanning').click()

    @staticmethod
    def tap_support():  # Тап на "Поддержка"
        driver.find_element(By.ID, 'ru.berizaryad.android.staging:id/btn_support').click()

    @staticmethod
    def tap_cross():  # Тап на "Крестик"
        driver.find_element(By.ID, 'ru.berizaryad.android.staging:id/btn_close').click()
