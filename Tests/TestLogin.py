import pytest

from Tests.TestBase import TestBase
from Pages.LoginPage import LoginPage
from Config.config import TestData


class TestLogin(TestBase):
    def test_login_page_title(self):
        self.loginPage = LoginPage(self.driver)
        # title = self.loginPage.get_title(TestData.LOGIN_PAGE_TITLE)
        assert TestData.LOGIN_PAGE_TITLE == self.loginPage.get_title(TestData.LOGIN_PAGE_TITLE)

    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
