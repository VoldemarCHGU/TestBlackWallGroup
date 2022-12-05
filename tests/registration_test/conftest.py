import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
import json

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.firefox.webdriver import WebDriver
from pages.main_functions import MAIN_URL

from pages.main_settings import *
MAIN_URL = "https://bitokk.biz/register"



def closing_everything(browser):
    # with allure.step("Фрагмент в конце теста"):
    #      allure.attach(browser.get_screenshot_as_png(),
    #                    name='screenshot',
    #                    attachment_type=AttachmentType.PNG)
    browser.close()
    browser.quit()


# def pytest_addoption(parser):
#     parser.addoption('--browser_name', action='store', default="chrome",
#                      help="Выберите браузер: 'chrome' or 'firefox'")
#     parser.addoption('--language', action='store', default="en",
#                      help="Введите язык для запуска теста...'")


def choose_browser():
    # browser_name = request.config.getoption("browser_name")
    browser_name = "chrome"
    if browser_name == "chrome":
        print("\nStart chrome browser for test..")
        # browser = webdriver.Chrome(executable_path='../../chromedriver.exe')
        browser = webdriver.Chrome(executable_path='chromedriver.exe')
    elif browser_name == "firefox":
        print("\nStart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    return browser


def browser_settings():
    """
    Настройка браузера перед запуском теста
    request : выбор браузера (по умолчанию хром)
    value : значение для авторизации по сессии/токену
    """
    browser: WebDriver
    browser = choose_browser()
    browser.maximize_window()
    browser.get(MAIN_URL)
    # for cookie in cookies:
    #     browser.add_cookie(
    #         {'name': cookie[0], 'value': cookie[1]})

    return browser



@pytest.fixture(scope='session')
def browser_set(request):
    try:
        print("\n___Start браузера для проверки регистрации")
        browser = browser_settings()
        yield browser
        print("\n___Закрытие браузера___")
    finally:
        closing_everything(browser)


