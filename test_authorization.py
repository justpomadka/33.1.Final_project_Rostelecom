import pytest

from .pages.authorization_page import AuthorizationPage
from .pages.password_recovery import PasswordRecoveryPage



@pytest.mark.autorization
def test_can_open_authorization_page(browser):
    link = "https://lk.rt.ru/"
    page = AuthorizationPage(browser, link)
    
    page.open()
   
    page.should_be_login_page()

@pytest.mark.autorization
def test_that_telephone_email_login_account_tabs_presented_on_page(browser):
    link = "https://lk.rt.ru/"
    page = AuthorizationPage(browser, link)
   
    page.open()
    
    page.should_have_tabs()

@pytest.mark.autorization
def test_that_telephone_tab_is_active_by_default(browser):
    link = "https://lk.rt.ru/"
    page = AuthorizationPage(browser, link)
    
    page.open()
    
    page.should_have_active_telephone_tab()

@pytest.mark.autorization
def test_that_logo_is_presented(browser):
    link = "https://lk.rt.ru/"
    page = AuthorizationPage(browser, link)
    
    page.open()
  
    page.should_have_logo()

@pytest.mark.autorization
def test_email_tab_is_active_when_email_is_entered_in_the_field(browser):
    link = "https://lk.rt.ru/"
    page = AuthorizationPage(browser, link)
    
    page.open()

    email = "ledi_night@gmail.com"
    
    page.enter_email(email)
   
    page.should_have_active_email_tab()

@pytest.mark.autorization
def test_login_tab_is_active_when_login_is_entered_in_the_field(browser):
    link = "https://lk.rt.ru/"
    page = AuthorizationPage(browser, link)
    
    page.open()

    login = "rtkid_16454169833426"
    
    page.enter_login(login)
    
    page.should_have_active_login_tab()

@pytest.mark.autorization
def test_account_tab_is_active_when_account_is_entered_in_the_field(browser):
    link = "https://lk.rt.ru/"
    page = AuthorizationPage(browser, link)
    
    page.open()

    account_number = "16454169833426"
 
    page.enter_login(account_number)
   
    page.should_have_active_account_tab()

@pytest.mark.autorization
def test_success_authorization_by_phone_number(browser):
    link = "https://lk.rt.ru/"
    page = AuthorizationPage(browser, link)
    
    page.open()

    phone = "9214578541"
    password = "Qwerty123"
    
    page.enter_phone(phone)
   
    page.enter_password(password)
    
    page.click_enter_button()
    
    page.should_have_opened_account_page()
    
    page.click_logout_button()

@pytest.mark.autorization
def test_success_authorization_by_email(browser):
    link = "https://lk.rt.ru/"
    page = AuthorizationPage(browser, link)
    
    page.open()

    email = "ledi_night@gmail.com"
    password = "Qwert123"
   
    page.enter_email(email)
    
    page.enter_password(password)
    
    page.click_enter_button()
    
    page.should_have_opened_account_page()
   
    page.click_logout_button()

@pytest.mark.autorization
def test_success_authorization_by_account_number(browser):
    link = "https://lk.rt.ru/"
    page = AuthorizationPage(browser, link)
  
    page.open()

    login = "rtkid_164169833426"
    password = "Fkfhj456"
   
    page.enter_login(login)
   
    page.enter_password(password)
    
    page.click_enter_button()
    
    page.should_have_opened_account_page()
    
    page.click_logout_button()

@pytest.mark.autorization
def test_show_error_message_in_case_of_wrong_phone_or_password(browser):
    link = "https://lk.rt.ru/"
    page = AuthorizationPage(browser, link)
   
    page.open()

    phone = "79215455156"
    password = "dfhv457Q"
   
    page.enter_phone(phone)
    
    page.enter_password(password)
   
    page.click_enter_button()
    "
    page.should_have_error_message()

@pytest.mark.autorization
def test_show_error_message_in_case_of_wrong_email_or_password(browser):
    link = "https://lk.rt.ru/"
    page = AuthorizationPage(browser, link)
   
    page.open()

    email = "ivanovgmail.com"
    password = "QWesfxscd78"
    
    page.enter_email(email)
  
    page.enter_password(password)
    
    page.click_enter_button()
    
    page.should_have_error_message()

@pytest.mark.autorization
def test_show_error_message_in_case_of_wrong_login_or_password(browser):
    link = "https://lk.rt.ru/"
    page = AuthorizationPage(browser, link)
   
    page.open()

    login = "rtkid_1684169833426"
    password = "Flk12314545"
    
    page.enter_login(login)
   
    page.enter_password(password)
    
    page.click_enter_button()
   
    page.should_have_error_message()

@pytest.mark.autorization
def test_recovery_password_page_opens(browser):
    link = "https://lk.rt.ru/"
    page = AuthorizationPage(browser, link)
    
    page.open()
  
    page.click_forgot_password_button()
    page2 = PasswordRecoveryPage(browser, browser.current_url)
    
    page2.should_be_password_recovery_page()

@pytest.mark.autorization
def test_that_telephone_email_login_account_tabs_presented_on_recovey_password_page(browser):
    link = "https://lk.rt.ru/"
    page = AuthorizationPage(browser, link)
    
    page.open()
    
    page.click_forgot_password_button()
    page2 = PasswordRecoveryPage(browser, browser.current_url)
   
    page2.should_have_tabs()
    
    page2.should_have_active_telephone_tab()

@pytest.mark.autorization
def test_that_recovey_password_page_has_login_form(browser):
    link = "https://lk.rt.ru/"
    page = AuthorizationPage(browser, link)
   
    page.open()
  
    page.click_forgot_password_button()
    page2 = PasswordRecoveryPage(browser, browser.current_url)
  
    page2.should_be_login_form()

@pytest.mark.autorization
def test_that_recovey_password_page_has_continue_button(browser):
    link = "https://lk.rt.ru/"
    page = AuthorizationPage(browser, link)
    
    page.open()
    
    page.click_forgot_password_button()
    page2 = PasswordRecoveryPage(browser, browser.current_url)
   
    page2.should_be_continue_button()

@pytest.mark.autorization
def test_that_recovey_password_page_has_back_button(browser):
    link = "https://lk.rt.ru/"
    page = AuthorizationPage(browser, link)
   
    page.open()
    
    page.click_forgot_password_button()
    page2 = PasswordRecoveryPage(browser, browser.current_url)
    
    page2.should_be_back_button()

