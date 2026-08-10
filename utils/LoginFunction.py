from pages import login_page
from pages.home_page import Home_page


def login(driver, username, password):
    homeP = Home_page(driver)
    loginP = login_page.Login_page(driver)

    homeP.click_main_login_button()
    loginP.enter_username(username)
    loginP.enter_password(password)
    loginP.click_login_button()
