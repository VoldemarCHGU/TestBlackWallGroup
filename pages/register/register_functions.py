import json
import os
import time
from datetime import datetime

from pages.base_page import BasePage
from collections import defaultdict
from pages.register.registor_locator import RegisterLocators
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver



class RegisterCheckFunctions(BasePage):
    def set_email(self, value):
        """
        Установка значения "Email"
        :param value: Устанавливаемое значение
        :return:
        """
        try:
            self.browser: WebDriver
            input_email = self.browser.find_element(*RegisterLocators.INPUT_EMAIL)
        except:
            assert False, "Отсутствует поле ввода Email"
        try:
            input_email.click()
            input_email.send_keys(value)
        except:
            assert False, "Не удалось установить Email"

    def set_password(self, value):
        """
        Установка значения "Пароль"
        :param value: Устанавливаемое значение
        :return:
        """
        try:
            self.browser: WebDriver
            input_pass = self.browser.find_element(*RegisterLocators.INPUT_PASS)
        except:
            assert False, "Отсутствует поле ввода пароля"
        try:
            input_pass.click()
            input_pass.send_keys(value)
        except:
            assert False, "Не удалось ввести Пароль"

    def set_repeat_pass(self, value):
        """
                Установка значения "Повтор пароля"
                :param value: Устанавливаемое значение
                :return:
                """
        try:
            self.browser: WebDriver
            input_compare_pass = self.browser.find_element(*RegisterLocators.INPUT_COMPARE_PASS)
        except:
            assert False, "Отсутствует поле ввода пароля"
        try:
            input_compare_pass.click()
            input_compare_pass.send_keys(value)
        except:
            assert False, "Не удалось ввести повторно пароль"

    def click_registration(self):
        try:
            self.browser: WebDriver
            btn_reg = self.browser.find_element(*RegisterLocators.BTN_REGISTER)
            btn_reg.click()
            time.sleep(2)
        except:
            assert False, "Не удалось найти кнопку регистрации"

    def check_lk(self):
        try:
            self.browser: WebDriver
            assert self.browser.current_url=="https://bitokk.biz/exchange-history-page", "Нет редиректа в ЛК"
            # тут проверка доп.локаторов ещё...
        except:
            assert False, "Редирект в ЛК не произведён"

