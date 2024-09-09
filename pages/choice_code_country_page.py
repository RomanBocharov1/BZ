from tests.conftest import driver

# Экран "Выбор кода страны"


class ChoiceCodeCountryPage:

    @staticmethod
    def choice_code_russia():  # Тап на код России
        driver.find_element('xpath', "//*[contains(@text,'(+7) Россия')]").click()
