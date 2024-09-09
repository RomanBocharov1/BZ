from selenium.webdriver.common.by import By
from tests.conftest import driver

# Экран подтверждения номера аппарата


class VerifyNumVendingPage:

    @staticmethod
    def tap_next():  # Тап на "Продолжить"
        driver.find_element(By.ID, 'ru.berizaryad.android.staging:id/btnContinue').click()

    @staticmethod
    def tap_cross():  # Тап на "Крестик"
        driver.find_element(By.ID, 'ru.berizaryad.android.staging:id/btn_close').click()

    @staticmethod
    def tap_support():  # Тап на "Поддержка"
        driver.find_element(By.ID, 'ru.berizaryad.android.staging:id/btn_support').click()

    @staticmethod
    def tap_back():  # Тап на "Назад"
        driver.find_element(By.ID, 'ru.berizaryad.android.staging:id/btnBack').click()

    @staticmethod
    def tap_scan_qr():  # Тап на "Сканировать QR"
        driver.find_element(By.ID, 'ru.berizaryad.android.staging:id/btnScanQr').click()

    @staticmethod
    def tap_take_charge():  # Тап на "Взять заряд"
        driver.find_element(By.ID, 'ru.berizaryad.android.staging:id/btMain').click()

