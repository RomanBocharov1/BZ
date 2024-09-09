import time
import random
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from pages.map_page import Map
from pages.side_menu_page import SideMenuPage
from pages.profile_page import ProfilePage
from pages.auth_input_number_page import system_numbersKeys


class Methods:

    def __init__(self, driver):
        self.driver = driver

    def send_keys(self, resource_id, number_or_keys):  # Ввод текста
        btn = self.driver.find_element(By.ID, resource_id)
        btn.click()
        btn.clear()
        btn.send_keys(number_or_keys)

    def tap_no_thanks(self, resource_id):  # тап на элемент
        self.driver.find_element(By.ID, resource_id).click()

    def swipe_from_middle_to_up(self):  # Свайп с середины экрана до верха экрана
        action = TouchAction(self.driver)
        action.press(x=539, y=1067).move_to(x=528, y=155).release().perform()

    def tap_on_screen(self):  # Тап на карту
        action = TouchAction(self.driver)
        action.press(x=539, y=1067)

    def tap_system_back(self):  # Системная кнопка "Назад"
        self.driver.press_keycode(4)

    def click_xpass(self, name, xpass_id):  # Найти элемент по xpath и тапнуть
        item_button = self.driver.find_element(name, xpass_id)
        item_button.click()

    def input_system_keys(self, phone):  # Ввод цифр через системную клавиатуру
        for i in range(len(phone)):
            number_from_phone = phone[i]
            keyboard_code = system_numbersKeys[number_from_phone]
            self.driver.press_keycode(keyboard_code)

    def generate_random_number(self):  # Генерация рандомного номера
        num_list = []
        while len(num_list) < 9:
            num = str(random.randint(0, 9))
            if not num in num_list:
                num_list.append(num)
        str_join = ''.join(num_list)
        random_number = '9' + str_join
        return random_number

    def drop_user(self):  # Флоу удаления юзера, начало пути - карта
        time.sleep(3)
        Map.open_side_menu()
        SideMenuPage.tap_profile()
        ProfilePage.tap_more()
        ProfilePage.tap_del_account()
        ProfilePage.tap_btn_confirm()
        assert self.driver.find_element(AppiumBy.XPATH, "//*[@text ='Твой аккаунт удален']")
        ProfilePage.tap_btn_ok()






