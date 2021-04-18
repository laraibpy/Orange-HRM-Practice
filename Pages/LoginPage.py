from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Config.config import TestData


class LoginPage(BasePage):
    email = (By.ID, "txtUsername")
    password = (By.ID, "txtPassword")
    login_btn = (By.ID, "btnLogin")

    """constructor"""
    def __init__(self, driver):
        # super.__init__(driver)
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """page actions"""
    # for getting page title
    def login_page_title(self, title):
        return self.get_title(title)

    # for logging in
    def do_login(self, username, password):
        self.do_send_keys(self.email, username)
        self.do_send_keys(self.password, password)
        self.do_click(self.login_btn)

