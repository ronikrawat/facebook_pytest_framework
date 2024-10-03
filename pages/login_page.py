from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, browser):
        self.browser = browser
        self.email_input = (By.ID, "email")
        self.password_input = (By.ID, "pass")
        self.login_button = (By.NAME, "login")

    def load(self):
        self.browser.get("https://www.facebook.com")

    def enter_email(self, email):
        self.browser.find_element(*self.email_input).send_keys(email)

    def enter_password(self, password):
        self.browser.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.browser.find_element(*self.login_button).click()
