from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class landing_page:
    landing_page_xpath = "//h2/span[contains(text(),'Welcome')]"

    def __init__(self, driver):
        self.driver = driver

    def is_landing_page_displayed(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH,self.landing_page_xpath))).is_displayed()