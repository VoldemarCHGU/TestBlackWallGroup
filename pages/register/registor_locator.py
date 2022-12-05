from selenium.webdriver.common.by import By


class RegisterLocators():
    LABEL_EMAIL = (By.XPATH, "//label[contains(text(), 'Email')]")
    INPUT_EMAIL = (By.NAME, "email")

    LABEL_PASS = (By.XPATH, "//label[contains(text(), 'Пароль')]")
    INPUT_PASS = (By.NAME, "password")

    LABEL_COMPARE_PASS = (By.XPATH, "//label[contains(text(), 'Подтвердите пароль')]")
    INPUT_COMPARE_PASS = (By.NAME, "compare-password")

    BTN_REGISTER = (By.CSS_SELECTOR, ".btn[data-test-id='test-button-register']")

    # Доп.локаторы
    # Текст в форме перед полями "Реистрация сделает работу ..."
    # всплывающие сообщения валидаторы "Пароль должен содержать цифры ..."
    # показ пароля
    # кнопка входа
    # хедеры, футеры