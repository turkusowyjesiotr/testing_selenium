import pytest
from pages.billing_address_page import BillingAddressPage
from pages.my_account_page import MyAccountPage
import allure


@allure.title("This modifying billing address test")
@pytest.mark.usefixtures("setup")
class TestUpdateBillingAddress:
    def test_update_billing_address(self):
        email = "testing@testing.test"
        password = "strong_password_strong_password"
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.log_in(email, password)
        billing_address_page = BillingAddressPage(self.driver)
        billing_address_page.edit_billing_address()
        billing_address_page.clear_inputs()
        billing_address_page.set_personal_data("John", "Johnson")
        billing_address_page.select_country("Poland")
        billing_address_page.set_address_data("Kwiatowa 1", "apt. 58", "00-001", "Warsaw")
        billing_address_page.set_phone_number("555-666-777")
        billing_address_page.save_billing_address()
        msg = "Address changed successfully"
        allure.attach(self.driver.get_screenshot_as_png())

        assert msg in billing_address_page.get_message_text()
