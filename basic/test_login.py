
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class TestLogin:
    # Define the website URL and the XPaths for the elements
    website_url = "https://ndosisimplifiedautomation.vercel.app/"
    main_login_button_xpath = "//div[@class='nav-user-section']"
    login_page_xpath = "//h2[@id='login-heading']"
    username_field_xpath = "//input[@id='login-email']"
    password_field_xpath = "//input[@id='login-password']"
    login_button_xpath = "//button[@id='login-submit']"
    landing_page_xpath = "//h2"


    @pytest.mark.sanity
    @pytest.mark.login
    @pytest.mark.critical
    def test_login(self):
        # start the browser and navigate to the website
        self.driver = webdriver.Chrome()
        self.driver.get(self.website_url)
        # instintiate WebDriverWait to wait 10 second for each element
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.main_login_button_xpath))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, self.login_page_xpath))).is_displayed()
        wait.until(EC.visibility_of_element_located((By.XPATH, self.username_field_xpath))).send_keys("nkwanyana@gmail.com")
        wait.until(EC.visibility_of_element_located((By.XPATH, self.password_field_xpath))).send_keys("@12345678")
        wait.until(EC.visibility_of_element_located((By.XPATH, self.login_button_xpath))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, self.landing_page_xpath))).is_displayed()

        # Quite driver
        self.driver.quit()

