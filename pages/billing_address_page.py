from selenium.webdriver import Keys
from locators import locators
from selenium.webdriver.support.select import Select
import allure


class BillingAddressPage:
    def __init__(self, driver):
        self.driver = driver

        # billing address page element
        self.reg_email_input = locators.BillingAddressLocators.reg_email_input
        self.reg_password_input = locators.BillingAddressLocators.reg_password_input
        self.addresses_link = locators.BillingAddressLocators.addresses_link
        self.edit_link = locators.BillingAddressLocators.edit_link
        self.first_name_input = locators.BillingAddressLocators.first_name_input
        self.last_name_input = locators.BillingAddressLocators.last_name_input
        self.country_select = locators.BillingAddressLocators.country_select
        self.address_input = locators.BillingAddressLocators.address_input
        self.address_optional_input = locators.BillingAddressLocators.address_optional_input
        self.postcode_input = locators.BillingAddressLocators.postcode_input
        self.city_input = locators.BillingAddressLocators.city_input
        self.phone_input = locators.BillingAddressLocators.phone_input
        self.save_address_button = locators.BillingAddressLocators.save_address_button
        self.message = locators.BillingAddressLocators.message

    @allure.step("Clearing old data")
    def clear_inputs(self):
        self.driver.find_element(*self.first_name_input).clear()
        self.driver.find_element(*self.last_name_input).clear()
        self.driver.find_element(*self.address_input).clear()
        self.driver.find_element(*self.address_optional_input).clear()
        self.driver.find_element(*self.postcode_input).clear()
        phone_placeholder = self.driver.find_element(*self.phone_input).get_attribute("value")
        for i in range(len(phone_placeholder)):
            self.driver.find_element(*self.phone_input).send_keys(Keys.BACKSPACE)
        city_placeholder = self.driver.find_element(*self.city_input).get_attribute("value")
        for i in range(len(city_placeholder)):
            self.driver.find_element(*self.city_input).send_keys(Keys.BACKSPACE)

    @allure.step("Navigating to billing address form")
    def edit_billing_address(self):
        self.driver.find_element(*self.addresses_link).click()
        self.driver.find_element(*self.edit_link).click()

    @allure.step("Passing in personal data (name, last name)")
    def set_personal_data(self, first_name, last_name):
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)

    @allure.step("Selecting country")
    def select_country(self, country):
        select = Select(self.driver.find_element(*self.country_select))
        select.select_by_visible_text(country)

    @allure.step("Passing in address")
    def set_address_data(self, street_address, address_optional, postcode, city):
        self.driver.find_element(*self.address_input).send_keys(street_address)
        self.driver.find_element(*self.address_optional_input).send_keys(address_optional)
        self.driver.find_element(*self.postcode_input).send_keys(postcode)
        self.driver.find_element(*self.city_input).send_keys(city)

    @allure.step("Setting phone number")
    def set_phone_number(self, number):
        self.driver.find_element(*self.phone_input).send_keys(number)

    @allure.step("Saving all changes to address form")
    def save_billing_address(self):
        self.driver.find_element(*self.save_address_button).click()

    def get_message_text(self):
        return self.driver.find_element(*self.message).text
