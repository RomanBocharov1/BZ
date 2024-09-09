from tests.conftest import driver

# Экран бокового меню


class SideMenuPage:

    @staticmethod
    def tap_profile():  # Тап на профиль
        driver.find_element('xpath', "//*[contains(@text,'Профиль')]").click()

    @staticmethod
    def tap_methods_payment():  # Тап на Способы оплаты
        driver.find_element('xpath', "//*[contains(@text,'Способы оплаты')]").click()

    @staticmethod
    def tap_stocks_partner():  # Тап на Акции партнеров
        driver.find_element('xpath', "//*[contains(@text,'Акции партнеров')]").click()

    @staticmethod
    def tap_tariff():  # Тап на Тарифы
        driver.find_element('xpath', "//*[contains(@text,'Тарифы')]").click()

    @staticmethod
    def tap_doc():  # Тап на Документы
        driver.find_element('xpath', "//*[contains(@text,'Документы')]").click()

    @staticmethod
    def tap_franchize():  # Тап на Франчайзинг
        driver.find_element('xpath', "//*[contains(@text,'Франчайзинг')]").click()

    @staticmethod
    def tap_support():  # Тап на Поддержка
        driver.find_element('xpath', "//*[contains(@text,'Поддержка')]").click()

    @staticmethod
    def tap_about():  # Тап на О приложении
        driver.find_element('xpath', "//*[contains(@text,'О приложении')]").click()




