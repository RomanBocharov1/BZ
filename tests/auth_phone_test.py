import time
import allure
from pages.map_page import Map
from pages.auth_input_number_page import AuthInputNumberPage
from pages.choice_code_country_page import ChoiceCodeCountryPage
from pages.input_verify_code_page import InputVerifyCodePage
from pages.choice_country_page import ChoiceCountryPage
from helpers.methods import Methods
from tests.conftest import driver


@allure.feature('Авторизация')
@allure.title('Авторизация через телефон')
def test_auth_by_phone():
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
    with allure.step('Тап на "Выбрать" на экране выбора страны'):
        ChoiceCountryPage.tap_select()  # если есть выбор страны, значит юзер новый
    time.sleep(3)
    with allure.step('Тап карту для закрытия плашки выбора способа оплаты'):
        ChoiceCountryPage.tap_map()
    with allure.step('Закрытие баннера подписки'):
        Map.close_banner_sub()
    drop = Methods(driver)
    drop.drop_user()









