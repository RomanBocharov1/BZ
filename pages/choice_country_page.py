from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from tests.conftest import driver

# Экран "Выбор страны"


class ChoiceCountryPage:

    @staticmethod
    def send_keys_input_field_search_for_filter(keys='Ро'): # Ввод в поле "Поиск" символов "Ро"
        btn = driver.find_element(By.ID, 'ru.berizaryad.android.staging:id/editTextNumber')
        btn.click()
        btn.clear()
        btn.send_keys(keys)

    @staticmethod
    def send_keys_input_field_search_random(keys='ОиGn56$%'): # Ввод в поле "Поиск" случайного набора символов
        btn = driver.find_element(By.ID, 'ru.berizaryad.android.staging:id/editTextNumber')
        btn.click()
        btn.clear()
        btn.send_keys(keys)

    @staticmethod
    def tap_select():  # Тап на "Выбрать"
        driver.find_element(By.ID, 'ru.berizaryad.android.staging:id/btnSelect').click()

    @staticmethod
    def tap_map():  # Тап на "Карту"
        driver.find_element(By.ID, 'ru.berizaryad.android.staging:id/touch_outside').click()

    @staticmethod
    def tap_check_box_kaz():  # Тап на чекбокс "Казахстан"
        driver.find_element(AppiumBy.XPATH, "//*[@bounds ='[940,886][1000,1006]'] ").click()

    @staticmethod
    def tap_check_box_kgz():  # Тап на чекбокс "Казахстан"
        driver.find_element(AppiumBy.XPATH, "//*[@bounds ='[933,716][996,842]'] ").click()

    @staticmethod
    def tap_check_box_rus():  # Тап на чекбокс "Россия"
        driver.find_element(AppiumBy.XPATH, "//*[@bounds ='[933,905][996,1031]'] ").click()
