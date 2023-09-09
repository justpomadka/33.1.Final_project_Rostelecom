from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators import AuthorizationByCodePageLocators
import time

class AuthorizationByCode(BasePage):

    def should_be_opened_authorization_by_code(self):
        self.should_be_authorization_by_code_message()
        self.should_be_form()
        self.should_be_get_code_button()

    def should_be_authorization_by_code_message(self):
        
        assert self.is_element_present(*AuthorizationByCodePageLocators.AUTHORIZATION_BY_CODE_MESSAGE)

    def should_be_form(self):
        
        assert self.is_element_present(*AuthorizationByCodePageLocators.WAY_OF_GETTING_CODE_FORM)

    def should_be_get_code_button(self):
      
        assert self.is_element_present(*AuthorizationByCodePageLocators.GET_CODE_BUTTON)

    def have_logo(self):
        assert self.is_element_present(*AuthorizationByCodePageLocators.LOGO)

    def enter_email(self, email):
        email_input = self.browser.find_element(*AuthorizationByCodePageLocators.WAY_OF_GETTING_CODE_FORM)
        email_input.send_keys(email)

    def enter_phone(self, phone):
        email_input = self.browser.find_element(*AuthorizationByCodePageLocators.WAY_OF_GETTING_CODE_FORM)
        email_input.send_keys(phone)

    def get_code_button(self):
        enter_button = self.browser.find_element(*AuthorizationByCodePageLocators.GET_CODE_BUTTON)
        enter_button.click()

    def enter_with_password_button(self):
        forgot_password_button = self.browser.find_element(*AuthorizationByCodePageLocators.ENTER_WITH_PASSWORD_BUTTON)
        forgot_password_button.click()

    def have_message_that_code_was_sent(self):
        assert self.browser.find_element(*AuthorizationByCodePageLocators.CODE_WAS_SENT_MESSAGE).text == \
               "Код подтверждения отправлен"
