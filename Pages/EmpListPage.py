
import time
from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Config.config import TestData
from Pages.CreateEmpPage import CreateEmpPage


class EmpListPage(BasePage):
    PIM = (By.LINK_TEXT, "PIM")
    employee_list = (By.LINK_TEXT, "Employee List")
    search_id = (By.NAME, 'empsearch[id]')
    search_btn = (By.ID, "searchBtn")
    search_result_id = (By.LINK_TEXT, CreateEmpPage.emp_id)
    check_box = (By.NAME, 'chkSelectRow[]')
    delete_btn = (By.ID, 'btnDelete')
    delete_popup = (By.ID, 'dialogDeleteBtn')
    rslt = (By.XPATH, "//td[contains(text(),'No Records Found')]")

    actual_emp_id = CreateEmpPage.emp_id
    """constructor"""
    def __init__(self, driver):
        # super.__init__(driver)
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """page actions"""
    # for getting page title
    # def add_emp_page_title(self, title):
    #     return self.get_title(title)

    # navigate to PIM Add emp page

    # for adding employee
    def search_employee(self, emp_id):
        self.do_click(self.PIM)
        time.sleep(2)
        self.clear(self.search_id)
        self.do_send_keys(self.search_id, emp_id)
        self.do_click(self.search_btn)

    def del_employee(self):
        self.do_click(self.check_box)
        self.do_click(self.delete_btn)
        time.sleep(5)
        self.do_click(self.delete_popup)

    def emp_not_avlbl(self):
        msg = self.get_element_text(self.rslt)
        assert msg == 'No Records Found'
        # assert self.get_input_text(self.search_result_id) not in employee_id