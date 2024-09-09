import time
import allure
from pages.map_page import Map
from pages.auth_input_number_page import AuthInputNumberPage
from pages.choice_code_country_page import ChoiceCodeCountryPage
from pages.input_verify_code_page import InputVerifyCodePage
from pages.choice_country_page import ChoiceCountryPage
from pages.input_data_card_kz_charge_page import InputDataCardKzchargePage
from pages.scan_qr_page import ScanQrPage
from pages.input_num_vending_page import InputNumVendingPage
from pages.verify_num_vending_page import VerifyNumVendingPage


@allure.feature('Авторизация')
@allure.title('Авторизация через телефон')
def test_rent_kz_charge():
    time.sleep(5)
    with allure.step('Тап на кнопку "Телефон"'):
        Map.tap_btn_phone()
    with allure.step('Тап на кнопку "Выбор кода страны"'):
        AuthInputNumberPage.tap_code_country()
    with allure.step('Выбор кода страны"Россия"'):
        ChoiceCodeCountryPage.choice_code_russia()
    with allure.step('Ввод рандомного номера телефона'):
        AuthInputNumberPage.input_num_phone()
    with allure.step('Тап на "Далее"'):
        AuthInputNumberPage.tap_button_next()
    time.sleep(3)
    with allure.step('Ввод кода'):
        InputVerifyCodePage.input_verify_code()
    time.sleep(5)
    with allure.step('Тап на чекбокс "Казахстан"'):
        ChoiceCountryPage.tap_check_box_kaz()
    with allure.step('Тап на "Выбрать" на экране выбора страны'):
        ChoiceCountryPage.tap_select()  # если есть выбор страны, значит юзер новый
    time.sleep(3)
    with allure.step('Тап на кнопку "Карта" на экране выбора способа оплаты'):
        Map.tap_button_card()
    with allure.step('Ввод данных карты'):
        InputDataCardKzchargePage.send_keys_card()
        InputDataCardKzchargePage.send_keys_date()
        InputDataCardKzchargePage.send_keys_cvv()
    with allure.step('Тап на кнопку "Взять заряд"'):
        Map.tap_take_charge()
    with allure.step('Дать пермишен на камеру'):
        ScanQrPage.tap_permission_allow_btn()
    with allure.step('Тап на кнопку "Не сканирует QR - код?"'):
        ScanQrPage.btn_not_scan()
    with allure.step('Тап на кнопку "Разрешить"'):
        InputNumVendingPage.permission_allow_btn()
    with allure.step('Ввод номера автомата'):
        InputNumVendingPage.send_keys_input_num_vending()
    with allure.step('Тап на кнопку "Взять заряд"'):
        VerifyNumVendingPage.tap_take_charge()

    # номер аренды и серийный номер банка берем через локаторы на фронте
    # для закрытия аренды использовать возвращатор релинков
    # def get_number_rent(self):
    #тест тест тест тест
    # def get_serial_pb(self):











