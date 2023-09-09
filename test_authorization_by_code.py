import pytest
from .pages.authorization_by_code  import AuthorizationByCodePage



@pytest.mark.code
def test_can_open_authorization_by_code_page(browser):
    link = "https://my.rt.ru/"
    page = AuthorizationByCodePage(browser, link)
   
    page.open()
  
    page.should_be_opened_authorization_by_code_page()


@pytest.mark.code
def test_that_code_send_when_telephone_number_entered(browser):
    link = "https://my.rt.ru/"
    page = AuthorizationByCodePage(browser, link)
    
    page.open()

    phone = "79241545265"
    page.enter_phone(phone)
    page.click_get_code_button()
   
    page.should_have_message_that_code_was_sent()


@pytest.mark.code
def test_that_code_send_when_email_entered(browser):
    link = "https://my.rt.ru/"
    page = AuthorizationByCodePage(browser, link)
    
    page.open()
    email = "ledi_night@gmail.com"
    page.enter_email(email)
    page.click_get_code_button()
   
    page.should_have_message_that_code_was_sent()


@pytest.mark.code
def test_that_logo_is_presented(browser):
    link = "https://my.rt.ru/"
    page = AuthorizationByCodePage(browser, link)
    
    page.open()
    
    page.should_have_logo()
