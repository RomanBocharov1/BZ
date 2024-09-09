from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from tests.conftest import driver

# Экран ввода данных карты в зоне КЗ_ЧАРДЖ


class InputDataCardKzchargePage:

    @staticmethod
    def send_keys_card():  # Ввод данных карты
        btn = driver.find_element(By.ID, 'ru.berizaryad.android.staging:id/edCardNumber')
        btn.click()
        btn.clear()
        btn.send_keys('5205000000003055')

    @staticmethod
    def send_keys_date():  # Ввод даты карты
        btn = driver.find_element(By.ID, 'ru.berizaryad.android.staging:id/edCardDate')
        btn.click()
        btn.clear()
        btn.send_keys('0830')

    @staticmethod
    def send_keys_cvv():  # Ввод даты cvv
        btn = driver.find_element(By.ID, 'ru.berizaryad.android.staging:id/edCardCvv')
        btn.click()
        btn.clear()
        btn.send_keys('566')

    @staticmethod
    def tap_no_thanks():  # тап на элемент
        driver.find_element(By.ID, 'ru.berizaryad.android.staging:id/btChargeOrder').click()







