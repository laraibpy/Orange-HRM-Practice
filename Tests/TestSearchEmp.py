import time

import pytest

from Pages.CreateEmpPage import CreateEmpPage
from Pages.EmpListPage import EmpListPage
# from TestMain import test_main
from Tests.TestBase import TestBase
from Pages.LoginPage import LoginPage
from Config.config import TestData


class TestSearchEmp(TestBase):
    def test_search_emp(self):
        self.createEmpPage = CreateEmpPage(self.driver)
        self.loginPage = LoginPage(self.driver)
        self.empListPage = EmpListPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        time.sleep(3)
        employee_id = self.createEmpPage.add_employee(TestData.FIRST_NAME, TestData.LAST_NAME)
        time.sleep(5)
        self.empListPage.search_employee(employee_id)
        time.sleep(3)
        self.empListPage.del_employee()
        time.sleep(3)
        self.empListPage.search_employee(employee_id)
        time.sleep(3)
        self.empListPage.emp_not_avlbl()
        time.sleep(4)
