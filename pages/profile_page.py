from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from tests.conftest import driver

# Экран профиля


class ProfilePage:

    @staticmethod
    def tap_more():  # Тап на "Еще"
        driver.find_element(AppiumBy.XPATH, "//*[@content-desc ='Ещё'] ").click()

    @staticmethod
    def tap_story_orders():  # Тап на "Историю аренд"
        driver.find_element(By.ID, 'ru.berizaryad.android.staging:id/btnHistory').click()

    @staticmethod
    def tap_back():  # Тап на "Назад"
        driver.find_element(AppiumBy.XPATH, "//*[@class ='android.widget.ImageButton'] ").click()

    @staticmethod
    def tap_del_account():  # Тап на "Удалить аккаунт"
        driver.find_element(AppiumBy.XPATH, "//*[@text ='Удалить аккаунт'] ").click()

    @staticmethod
    def tap_btn_confirm():  # Тап на "Удалить"
        driver.find_element(By.ID, 'ru.berizaryad.android.staging:id/btnConfirm').click()

    @staticmethod
    def tap_btn_ok():  # Тап на "Хорошо"
        driver.find_element(By.ID, 'ru.berizaryad.android.staging:id/btnOk').click()











