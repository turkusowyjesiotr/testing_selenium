from locators import locators
from selenium.webdriver.common.keys import Keys
import allure


class MyAccountPage:
    def __init__(self, driver):
        self.driver = driver

        # my account page elements
        self.username_input = locators.MyAccountPage.username_input
        self.password_input = locators.MyAccountPage.password_input
        self.reg_email_input = locators.MyAccountPage.reg_email_input
        self.reg_password_input = locators.MyAccountPage.reg_password_input
        self.logout_link = locators.MyAccountPage.logout_link
        self.error_msg = locators.MyAccountPage.error_msg

    @allure.step("Opening page")
    def open_page(self):
        self.driver.get('http://seleniumdemo.com/?page_id=7')

    @allure.step("Passing in username and password to log in")
    def log_in(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.password_input).send_keys(Keys.ENTER)

    @allure.step("Passing in username and password to register new account")
    def create_account(self, email, password):
        self.driver.find_element(*self.reg_email_input).send_keys(email)
        self.driver.find_element(*self.reg_password_input).send_keys(password)
        self.driver.find_element(*self.reg_password_input).send_keys(Keys.ENTER)

    def is_logout_link_displayed(self):
        return self.driver.find_element(*self.logout_link).is_displayed()

    def get_error_msg(self):
        return self.driver.find_element(*self.error_msg).text
