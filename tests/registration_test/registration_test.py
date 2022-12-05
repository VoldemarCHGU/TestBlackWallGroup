import time
import pytest
from pages.register.register_functions import *


@pytest.mark.registration
class TestRegistration():

    def test_positive_reg(self, browser_set):
        browser_set: WebDriver
        page = RegisterCheckFunctions(browser_set)
        page.set_email("1TTest1123123123QWEASD1@mail.ru")
        page.set_password("1TTest1123123123QWEASD1")
        page.set_repeat_pass("1TTest1123123123QWEASD1")
        page.click_registration()
        page.check_lk()





