import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

from TestData.Data import Testdata
from TestData.LoginData import LoginPageData


class Common:
    def __init__(self, driver):  # Class constructor
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, 30).until(EC.title_is(title))
        return self.driver.title

    def login_page(self):  # General login method for all the testcases
        self.driver.find_element(By.CSS_SELECTOR, "[id='login_form_username']").send_keys(Testdata.username)
        self.driver.find_element(By.CSS_SELECTOR, "[name='password']").send_keys(Testdata.password)
        self.driver.find_element(By.CSS_SELECTOR, "[class='btn btn-lg btn-primary btn-block']").click()

    @pytest.fixture(params=LoginPageData.gettestdata("Testcase2"))
    def getData(self, request):
        return request.param

    def selectOptionByText(self, locator, text):
        sel = Select(self.driver.find_element(*locator))
        sel.select_by_visible_text(text)

    def confirmation_alert(self):
        obj = self.driver.switch_to.alert
        obj.accept()
