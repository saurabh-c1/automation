import time

import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class RegisterCoursesPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators :-
    _search_box = "//input[contains(@id, 'search')]"
    _course = "//div[contains(@id, 'course-list')]//following::h4[contains(text(), '{0}')]"
    _search_button = "//button[contains(@type, 'submit')]"
    _all_courses = "course-list"
    _enroll_button = "//button[contains(text(), 'Enroll in Course')]"
    _cc_num = "//input[contains(@placeholder,'Card Number')]"
    _cc_exp = "//input[contains(@placeholder,'MM / YY')]"
    _cc_cvv = "//input[contains(@placeholder,'Security Code')]"
    _submit_enroll = "//button[contains(@class, 'zen-subscribe')]"
    _enroll_error_message = "//span[contains(text(), 'Your card number is incorrect.')]"
    _enroll_error_message1 = "//div[contains(@class, 'alert')]//following-sibling::p"

    def enterCourseName(self, name):
        self.sendKeys(name, locator=self._search_box, locatorType="xpath")
        self.elementClick(locator=self._search_button, locatorType="xpath")

    def selectCourseToEnroll(self, courseName):
        self.elementClick(locator=self._course.format(courseName), locatorType="xpath")

    def clickOnEnrollButton(self):
        self.elementClick(locator=self._enroll_button, locatorType="xpath")

    def enterCardNum(self, num):
        time.sleep(2)
        self.SwitchFrameByIndex(self._cc_num, locatorType="xpath")
        self.sendKeysWhenReady(num, locator=self._cc_num, locatorType="xpath")
        self.switchToDefaultContent()

    def enterCardExp(self, exp):
        self.SwitchFrameByIndex(self._cc_exp, locatorType="xpath")
        self.sendKeys(exp, locator=self._cc_exp, locatorType="xpath")
        self.switchToDefaultContent()

    def enterCardCVV(self, cvv):
        self.SwitchFrameByIndex(self._cc_cvv, locatorType="xpath")
        self.sendKeys(cvv, locator=self._cc_cvv, locatorType="xpath")
        self.switchToDefaultContent()

    def clickEnrollSubmitButton(self):
        self.elementClick(locator=self._submit_enroll, locatorType="xpath")

    def enterCreditCardInformation(self, num, exp, cvv):
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)

    def enrollCourse(self, num="", exp="", cvv=""):
        self.clickOnEnrollButton()
        self.webScroll(direction="down")
        self.enterCreditCardInformation(num, exp, cvv)
        self.clickEnrollSubmitButton()

    def verifyEnrollFailed(self):
        messageElement = self.waitForElement(self._enroll_error_message or self._enroll_error_message1, locatorType="xpath")
        result = self.isElementDisplayed(element=messageElement)
        return not result
