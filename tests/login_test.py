import allure
import pytest
from pages.my_account_page import MyAccountPage


@allure.title("This is logging in test")
@pytest.mark.usefixtures("setup")
class TestLogIn:
    def test_log_in_passed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        username = "testing@testing.test"
        password = "strong_password_strong_password"
        my_account_page.log_in(username, password)
        allure.attach(self.driver.get_screenshot_as_png())

        assert my_account_page.is_logout_link_displayed()

    def test_log_in_failed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        username = "testing@testing.test"
        password = "wrong_password"
        my_account_page.log_in(username, password)
        msg = "ERROR: Incorrect username or password."
        allure.attach(self.driver.get_screenshot_as_png())

        assert msg in my_account_page.get_error_msg()

