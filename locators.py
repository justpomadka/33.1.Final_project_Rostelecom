from selenium.webdriver.common.by import By

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

    TELEPHONE_TAB = (By.CSS_SELECTOR, "#t-btn-tab-phone")
    TELEPHONE_TAB_ACTIVE = (By.CSS_SELECTOR, '#t-btn-tab-phone.rt-tab--active')
    EMAIL_TAB = (By.CSS_SELECTOR, "#t-btn-tab-mail")
    EMAIL_TAB_ACTIVE = (By.CSS_SELECTOR, '#t-btn-tab-mail.rt-tab--active')
    LOGIN_TAB = (By.CSS_SELECTOR, "#t-btn-tab-login")
    LOGIN_TAB_ACTIVE = (By.CSS_SELECTOR, '#t-btn-tab-login.rt-tab--active')
    ACCOUNT_TAB = (By.CSS_SELECTOR, "#t-btn-tab-ls")
    ACCOUNT_TAB_ACTIVE = (By.CSS_SELECTOR, '#t-btn-tab-ls.rt-tab--active')
    USERNAME_FORM = (By.CSS_SELECTOR, '.rt-input__input[id="username"]')
    PASSWORD_FORM = (By.CSS_SELECTOR, '.rt-input__input[id="password"]')
    ENTER_BUTTON = (By.CSS_SELECTOR, 'button[id="kc-login"]')
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, 'a[id = "kc-register"]')
    AUTHORIZATION_MESSAGE = (By.CSS_SELECTOR, 'h1.card-container__title')
    LOGO = (By.CSS_SELECTOR, '.rt-logo.what-is-container__logo')
    INVITATION_MESSAGE = (By.CSS_SELECTOR, '[class ="color_black text-align-center n-header H2"]')
    # INVITATION_MESSAGE = (By.XPATH, '// *[ @ id = "app"] / main / div / div[2] / div[1] / h3[1]')

    ERROR_MESSAGE = (By.CSS_SELECTOR, '[id = "form-error-message"]')
    FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR, '.login-form__forgot-pwd--animated')
    FORGOT_PASSWORD_BUTTON = (By.CSS_SELECTOR, '#forgot_password')
    LOGOUT_BUTTON = (By.CSS_SELECTOR, '#logout-btn')
    ACCOUNT_ICON = (By.CSS_SELECTOR, '.sc-bvFjSx.iqOiiv')
    EXIT = (By.CSS_SELECTOR, '[class="sc-dkPtRN lgHXyI sc-dlVxhl bLVPuw"]')

class PasswordRecoveryPageLocators():
    LOGO = (By.CSS_SELECTOR, '.rt-logo.main-header__logo')
    MESSAGE_ABOUT_PASSWORD_RECOVERY = (By.CSS_SELECTOR, '.card-container__title')
    TELEPHONE_TAB = (By.CSS_SELECTOR, "#t-btn-tab-phone")
    TELEPHONE_TAB_ACTIVE = (By.CSS_SELECTOR, '#t-btn-tab-phone.rt-tab--active')
    EMAIL_TAB = (By.CSS_SELECTOR, "#t-btn-tab-mail")
    EMAIL_TAB_ACTIVE = (By.CSS_SELECTOR, '#t-btn-tab-mail.rt-tab--active')
    LOGIN_TAB = (By.CSS_SELECTOR, "#t-btn-tab-login")
    LOGIN_TAB_ACTIVE = (By.CSS_SELECTOR, '#t-btn-tab-login.rt-tab--active')
    ACCOUNT_TAB = (By.CSS_SELECTOR, "#t-btn-tab-ls")
    ACCOUNT_TAB_ACTIVE = (By.CSS_SELECTOR, '#t-btn-tab-ls.rt-tab--active')
    USERNAME_FORM = (By.CSS_SELECTOR, '.rt-input__input[id="username"]')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, '#reset')
    BACK_BUTTON = (By.CSS_SELECTOR, '#reset-back')

class RegistrationPageLocators():
    REGISTRATION_MESSAGE = (By.CSS_SELECTOR, '.card-container__title')
    LOGO = (By.CSS_SELECTOR, '.main-header__logo')
    NAME_FORM = (By.CSS_SELECTOR, '[name="firstName"]')
    SURNAME_FORM = (By.CSS_SELECTOR, '[name="lastName"]')
    USERNAME_FORM = (By.CSS_SELECTOR, '#address')
    PASSWORD_FORM = (By.CSS_SELECTOR, '#password')
    CONFIRMATION_PASSWORD_FORM = (By.CSS_SELECTOR, '#password-confirm')
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, '[name = "register"]')
    NAME_ERROR_MESSAGE = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/span')
    SURNAME_ERROR_MESSAGE = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span')
    PASSWORD_ERROR_MESSAGE = (By.XPATH,'//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span')
    PASSWORD_CONFIRM_ERROR_MESSAGE = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/span')
    MESSAGE_THAT_ACCOUNT_ALREADY_EXISTS = (By.CSS_SELECTOR, '.card-modal__title')
    MESSAGE_TO_CONFIRM_EMAIL = (By.CSS_SELECTOR, '.card-container__title')

class AuthorizationByCodePageLocators():
    AUTHORIZATION_BY_CODE_MESSAGE = (By.CSS_SELECTOR, '.card-container__title')
    LOGO = (By.CSS_SELECTOR, '.what-is-container__logo-container')
    WAY_OF_GETTING_CODE_FORM = (By.CSS_SELECTOR, '#address')
    GET_CODE_BUTTON = (By.CSS_SELECTOR, '#otp_get_code')
    ENTER_WITH_PASSWORD_BUTTON = (By.CSS_SELECTOR, '#standard_auth_btn')
    CODE_WAS_SENT_MESSAGE = (By.CSS_SELECTOR, '.card-container__title')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user
