import random
import pytest
from pages.my_account_page import MyAccountPage
import allure


@allure.title("This is creating new account test")
@pytest.mark.usefixtures("setup")
class TestCreateAccount:
    def test_create_account_passed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        email = f"testing{random.randint(0, 10000)}@testing.test"
        password = "strong_password"
        my_account_page.create_account(email, password)
        allure.attach(self.driver.get_screenshot_as_png())

        assert my_account_page.is_logout_link_displayed()

    def test_create_account_failed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        email = "testing@testing.test"
        password = "strong_password_strong_password"
        my_account_page.create_account(email, password)
        msg = "Error: An account is already registered with your email address. Please log in."
        allure.attach(self.driver.get_screenshot_as_png())

        assert msg in my_account_page.get_error_msg()
