import logging
from traceback import print_stack

import utilities.custom_logger as cl
from base.selenium_driver import SeleniumDriver


class CheckStatus(SeleniumDriver):
    log = cl.customLogger(logging.INFO)

    def __init__(self, driver):
        """
        Init CheckPoint class
        :param driver:
        """
        super(CheckStatus, self).__init__(driver)
        self.resultList = []

    def setResult(self, result, resultMessage):
        try:
            if result is not None:
                if result:
                    self.resultList.append("PASS")
                    self.log.info("### VERIFICATION SUCCESSFUL :: " + resultMessage)
                else:
                    self.resultList.append("FAIL")
                    self.log.error("### VERIFICATION FAILED :: " + resultMessage)
                    self.screenShot(resultMessage)
            else:
                self.resultList.append("FAIL")
                self.log.error("### VERIFICATION FAILED :: " + resultMessage)
                self.screenShot(resultMessage)
        except:
            self.resultList.append("FAIL")
            self.log.error(":#: EXCEPTION OCCURRED :#:")
            self.screenShot(resultMessage)
            print_stack()

    def mark(self, result, resultMessage):
        """
        Mark the result of verification point in a test case
        :param result:
        :param resultMessage:
        :return:
        """
        self.setResult(result, resultMessage)

    def markFinal(self, testName, result, resultMessage):
        """
        Mark the final result of the verification point in a test case
        This need to be called at least once in a test case
        This should be the final test status of the test case
        :param testName:
        :param result:
        :param resultMessage:
        :return:
        """
        self.setResult(result, resultMessage)
        if 'FAIL' in self.resultList:
            self.log.error(testName + "### TEST FAILED")
            self.resultList.clear()
            assert True == False
        else:
            self.log.info(testName + "### TEST SUCCESSFUL")
            self.resultList.clear()
            assert True == True
        print()
