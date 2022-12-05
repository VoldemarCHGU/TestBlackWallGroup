# import time
# import contextlib
# import allure
# from allure_commons.types import AttachmentType
# from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver


from .main_settings import MAIN_URL


class BasePage():
    def __init__(self, browser, url=MAIN_URL):
        self.browser = browser

        # self.url = url.strip()
        # self.url = url.get("link_page").strip()
        # check_link(MAIN_URL)
        # self.open_url()

    # def attach_screenshot(self, step, name):
    #     with allure.step(step):
    #         allure.attach(MAIN_URL + self.url,
    #                       name=name)
    #         allure.attach(self.browser.get_screenshot_as_png(),
    #                       name='screenshot_'+step+'_'+name,
    #                       attachment_type=AttachmentType.PNG)

    def open_url(self):
        """
        открывает ссылку внутри (авторизированному пользователю)
        :return:
        """
        self.browser: WebDriver
        url = MAIN_URL
        self.browser.get(url)

    def is_element_present(self, how, what, timeout=5):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
            # self.browser.find_element(how, what)
        except:
            return False
        return True


    def проверка_url_в_адресной_строке(self, url):
        self.ожидание_прогрузки_страницы()
        current_url = self.browser.current_url
        assert url == current_url, \
            f"""Не та страница
            ♦Ожидалось: {url}
            ♦Открылось: {current_url}"""


    def проверка_обновления(self):
        pass


    # def проверка_на_ошибку_на_странице(self):
    #     self.browser: WebDriver
    #     a = self.browser.get_cookies()
    #     pass