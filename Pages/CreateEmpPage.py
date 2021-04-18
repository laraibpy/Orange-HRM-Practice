import time

from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Config.config import TestData


class CreateEmpPage(BasePage):

    PIM = (By.LINK_TEXT, "PIM")
    add_btn = (By.ID, "btnAdd")
    first_name = (By.ID, "firstName")
    last_name = (By.ID, "lastName")
    save_btn = (By.ID, "btnSave")
    emp_id = (By.ID, "employeeId")
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
    def add_employee(self, firstname, lastname):
        time.sleep(3)
        self.do_click(self.PIM)
        time.sleep(2)
        self.do_click(self.add_btn)
        self.do_send_keys(self.first_name, firstname)
        self.do_send_keys(self.last_name, lastname)
        employ_id = self.get_input_text(self.emp_id)
        self.do_click(self.save_btn)
        return employ_id


