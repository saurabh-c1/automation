"""
BASE CLASS IMPLEMENTATION :-
It implements methods which are common to all the pages throughtout the application
This class needs to be inherited by all the page classes
This should not be used by creating object instances
"""
from base.selenium_driver import SeleniumDriver
from traceback import print_stack
from utilities.util import Util


class BasePage(SeleniumDriver):

    def __init__(self, driver):
        """
        Init BasePage class
        :param driver:
        :return
            None
        """
        super(BasePage, self).__init__(driver)
        self.driver = driver
        self.util = Util()

    def verifyPageTitle(self, titleToVerify):
        try:
            actualTitle = self.getTitle()
            return self.util.verifyTextContains(actualTitle, titleToVerify)
        except:
            self.log.error("Failed to get page title")
            print_stack()
            return False
