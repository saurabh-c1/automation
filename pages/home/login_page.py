import time
from base.basepage import BasePage
import logging
import utilities.custom_logger as cl
from pages.home.navigation_page import NavigationPage


class LoginPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    # LOCATORS :-
    _login_link = "//a[contains(@href, 'login')]"
    _email_field = "email"
    _password_field = "password"
    _login_button = "//input[contains(@type, 'submit')]"

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="xpath")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")

    def clearFields(self):
        emailField = self.getElement(locator=self._email_field)
        emailField.clear()
        passwordField = self.getElement(locator=self._password_field)
        passwordField.clear()

    def login(self, email="", password=""):
        self.clickLoginLink()
        self.clearFields()
        self.enterEmail(email)
        self.enterPassword(password)
        time.sleep(2)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("dropdownMenu1", locatorType="id")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//span[contains(text(), 'Your username or "
                                       "password is invalid. Please try again.')]", locatorType="xpath")
        return result

    def verifyLoginTitle(self):
        return self.verifyPageTitle("Google")

    def logout(self):
        self.nav.navigateToUserSettingsIcon()
        self.elementClick(locator="//a[contains(@href, 'logout')]", locatorType="xpath")
