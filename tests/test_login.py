import time

import allure
import pytest

from utils.config_properties import ReadConfig_CommonDetails
from pages.home_page import Home_page
from pages.login_page import Login_page
from pages.landing_page import landing_page


class Test_Login:
    dev_url = ReadConfig_CommonDetails().getDevUrl()
    username = ReadConfig_CommonDetails().getUsername()
    password = ReadConfig_CommonDetails().getPassword()


    @pytest.mark.sanity
#   @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self, setup):
        self.driver = setup
        homeP = Home_page(self.driver)
        loginP = Login_page(self.driver)
        landingP =landing_page(self.driver)

        self.driver.get(self.dev_url)
        self.driver.maximize_window()
        allure.attach(self.driver.get_screenshot_as_png(), name="Login Page", attachment_type=allure.attachment_type.PNG)

        homeP.click_main_login_button()
        loginP.enter_username(self.username)
        loginP.enter_password(self.password)
        loginP.click_login_button()
        landingP.is_landing_page_displayed()
        allure.attach(self.driver.get_screenshot_as_png(), name="Landing Page", attachment_type=allure.attachment_type.PNG)


        time.sleep(5)
