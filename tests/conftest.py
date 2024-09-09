from appium import webdriver


# коннект с Аппиум
desired_capabilities = {
    "automationName": "Appium",
    "platformName": "Android",
    "platformVersion": "10",
    "deviceName": "Android Emulator",
    "app": "/Users/roman/PycharmProjects/bz_auto_tests/7938_stage.apk",
    "noReset": "false",  # сохранение кеша, не сбрасывает кэш при выходе из теста
    "fullReset": "false"  # полный сброс данных + удаление прилки
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',
                          desired_capabilities=desired_capabilities)
driver.implicitly_wait(5)






