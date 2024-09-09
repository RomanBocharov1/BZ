from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from tests.conftest import driver

# Экран карты


class Map:

    @staticmethod
    def tap_no_thanks():  # Тап на "Нет, спасибо" на геопермишене
        driver.find_element(By.ID, 'android:id/button2').click()

    @staticmethod
    def tap_btn_phone():  # Тап на кнопку "Телефон" на плашке авторизации
        driver.find_element(By.ID, 'ru.berizaryad.android.staging:id/phoneBtnInclusion').click()

    @staticmethod
    def tap_take_charge():  # Тап на кнопку "Взять заряд"
        driver.find_element(By.ID, 'ru.berizaryad.android.staging:id/btTakePowerBank').click()

    @staticmethod
    def tap_fine_banner_subscription():  # Тап на "Понятно" на баннере подписки
        driver.find_element(By.ID, 'ru.berizaryad.android.staging:id/button').click()

    @staticmethod
    def tap_system_back():  # Тап на системную "Назад"
        driver.press_keycode(4)

    @staticmethod
    def tap_map():  # Тап на "Карту"
        driver.find_element(By.ID, 'ru.berizaryad.android.staging:id/touch_outside').click()

    @staticmethod
    def open_side_menu():  # Открытие бокового меню свайпом
        action = TouchAction(driver)
        action.long_press(x=13, y=844, duration=3).move_to(x=528, y=901).release().perform()

    @staticmethod
    def tap_add_dso():  # Тап на "Добавить" на плашке "Добавь способ оплаты"
        driver.find_element(By.ID, 'ru.berizaryad.android.staging:id/btnAdd').click()

    @staticmethod
    def tap_close_dso():  # Тап на "Закрыть" на плашке "Добавь способ оплаты"
        driver.find_element(AppiumBy.XPATH, "//*[@content-desc ='Закрыть'] ").click()

    @staticmethod
    def close_banner_sub():  # Закрыть баннер подписки на карте
        driver.find_element(By.ID, 'ru.berizaryad.android.staging:id/closeImageView').click()

    @staticmethod
    def tap_button_card():  # Тап на кнопку "Карта" на экране выбора способа оплаты
        driver.find_element(By.ID, 'ru.berizaryad.android.staging:id/btBankCard').click()
















