import pytest

from Pages.CreateEmpPage import CreateEmpPage
from Tests.TestBase import TestBase
from Pages.LoginPage import LoginPage
from Config.config import TestData
# from Tests.TestLogin import TestLogin


class TestCreateEmp(TestBase):
    def test_create_emp(self):
        self.createEmpPage = CreateEmpPage(self.driver)
        self.loginPage = LoginPage(self.driver)
        # TestLogin.test_login(self)
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.createEmpPage.add_employee(TestData.FIRST_NAME, TestData.LAST_NAME)

