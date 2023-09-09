
import pytest

from .pages.authorization_page import AuthorizationPage
from .pages.registration import RegistrationPage



@pytest.mark.registration
def test_can_open_registration_page(browser):
    link = "https://lk.rt.ru/"
    page = AuthorizationPage(browser, link)
    
    page.open()
   
    page.click_registration_button()

    page2 = RegistrationPage(browser,browser.current_url)
    page2.should_be_message_about_registration()

@pytest.mark.registration
def test_that_all_input_forms_presented_on_registration_page(browser):
    link = "https://lk.rt.ru/"
    page = AuthorizationPage(browser, link)
   
    page.open()
  
    page.click_registration_button()

    page2 = RegistrationPage(browser, browser.current_url)
    
    page2.should_be_message_about_registration()
   
    page2.should_be_name_surname_login_password_confirm_password_forms()

@pytest.mark.registration
def test_that_logo_is_presented(browser):
    link = "https://lk.rt.ru/"
    page = AuthorizationPage(browser, link)
  
    page.open()
   
    page.click_registration_button()

    page2 = RegistrationPage(browser, brow
    page2.should_have_logo()

@pytest.mark.registration
def test_show_error_message_in_case_name_is_entered_not_in_сyrillic(browser):
    link = "https://lk.rt.ru/"
    page = AuthorizationPage(browser, link)
    
    page.open()
   
    page.click_registration_button()

    page2 = RegistrationPage(browser, browser.current_url)
    name = "Ivan"
  
    page2.enter_name(name)
     
    page2.should_have_name_error_message()

@pytest.mark.registration
def test_show_error_message_in_case_surname_is_entered_not_in_сyrillic(browser):
    link = "https://lk.rt.ru/"
    page = AuthorizationPage(browser, link)
    
    page.open()
   
    page.click_registration_button()

    page2 = RegistrationPage(browser, browser.current_url)
    surname = "Ivanov"
  
    page2.enter_surname(surname)
     
    page2.should_have_surname_error_message()

@pytest.mark.registration
def test_show_error_message_in_case_password_shorter_then_8_simbols(browser):
    link = "https://lk.rt.ru/"
    page = AuthorizationPage(browser, link)
   
    page.open()
    
    page.click_registration_button()

    page2 = RegistrationPage(browser, browser.current_url)
    password = "12312"
    
    page2.enter_password(password)
    
    page2.should_have_error_message_that_password_should_be_more_then_8_symbols()

@pytest.mark.registration
def test_show_error_message_in_case_password_does_not_contain_capital_letters(browser):
    link = "https://lk.rt.ru/"
    page = AuthorizationPage(browser, link)
    
    page.open()
   
    page.click_registration_button()

    page2 = RegistrationPage(browser, browser.current_url)
    name = "Иван"
    password = "qwqawa123567"
    
    page2.enter_password(password)
   
    page2.should_have_error_message_that_password_does_not_contain_capital_letters()

@pytest.mark.registration
def test_show_error_message_in_case_password_does_not_contain_small_letters(browser):
    link = "https://lk.rt.ru/"
    page = AuthorizationPage(browser, link)
    
    page.open()
   
    page.click_registration_button()

    page2 = RegistrationPage(browser, browser.current_url)
    name = "Иван"
    password = "QWEERTY123567"
   
    page2.enter_password(password)
    
    page2.should_have_error_message_that_password_does_not_contain_small_letters()

@pytest.mark.registration
def test_show_error_message_in_case_password_contains_cyrrilics_letters(browser):
    link = "https://lk.rt.ru/"
    page = AuthorizationPage(browser, link)
   
    page.open()
    
    page.click_registration_button()

    page2 = RegistrationPage(browser, browser.current_url)
    name = "Иван"
    password = "вроаои123567"
    
    page2.enter_password(password)
    
    page2.should_have_error_message_that_password_must_contain_only_latin_letters()

@pytest.mark.registration
def test_show_error_message_in_case_of_password_and_confirmation_password_dont_match(browser):
    link = "https://lk.rt.ru/"
    page = AuthorizationPage(browser, link)
    
    page.open()
    
    page.click_registration_button()

    page2 = RegistrationPage(browser, browser.current_url)
    password = "Katya123567"
    confirm_password = "Atya12356789"
    
    page2.enter_password(password)
   
    page2.enter_confirmation_of_password(confirm_password)
    
    page2.click_registration_button()
    
    page2.should_have_error_message_that_passwords_dont_match()

@pytest.mark.registration
def test_show_message_that_account_already_exists_if_data_of_existing_accoun_entered_for_registration(browser):
    link = "https://lk.rt.ru/"
    page = AuthorizationPage(browser, link)
   
    page.open()
    
    page.click_registration_button()

    page2 = RegistrationPage(browser, browser.current_url)
    password = "Qwerty123
    name = "Иван"
    surname = "Иванов"
    email = "ivaii@gmail.com"

    page2.enter_name(name)
    page2.enter_surname(surname)
    page2.enter_email(email)
    
    page2.enter_password(password)
    page2.enter_confirmation_of_password(password)
    
    page2.click_registration_button()
   
    page2.should_have_message_that_account_already_exists()

@pytest.mark.registration
def test_register_new_user(browser):
    link = "https://lk.rt.ru/"
    page = AuthorizationPage(browser, link)
    
    page.open()
    
    page.click_registration_button()

    page2 = RegistrationPage(browser, browser.current_url)
    password = "Qwerty123"
    name = "Иван"
    surname = "Иванов"
    
    email = str(time.time()) + "@gmail.com"
   
    page2.register_new_user(name, surname, email, password)
 
    page2.should_have_message_to_confirm_email_of_new_user()
