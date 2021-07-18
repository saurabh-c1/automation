"""
UTIL CLASS IMPLEMENTATION:-
All most commonly used utilities should be implemented in this class

Example:
    name = self.util.getUniqueName()
"""
import time
import traceback
import random
import string
import utilities.custom_logger as cl
import logging


class Util(object):
    log = cl.customLogger(logging.INFO)

    def sleep(self, sec, info=""):
        """
        Program wait for the specified amount of time
        :param sec:
        :param info:
        :return:
        """
        if info is not None:
            self.log.info("Wait :: " + str(sec) + " seconds for " + info)
        try:
            time.sleep(sec)
        except InterruptedError:
            traceback.print_stack()

    def getAlphaNumeric(self, length, type="letters"):
        """
        Get random string of characters

        :param length:
        :param type:
        :return:
        """
        alpha_num = ''
        if type == 'lower':
            case = string.ascii_lowercase
        elif type == 'upper':
            case = string.ascii_uppercase
        elif type == 'digits':
            case = string.digits
        elif type == 'mix':
            case = string.ascii_letters + string.digits
        else:
            case = string.ascii_letters
        return alpha_num.join(random.choice(case) for i in range(length))

    def getUniqueName(self, charCount=10):
        """
        Get a unique name
        :param charCount:
        :return:
        """
        return self.getAlphaNumeric(charCount, 'lower')

    def getUniqueNameList(self, listSize=5, itemLength=None):
        """
        get a list of valid email ids

        :param listSize: default size is 5 names in a list
        :param itemLength:
        :return:
        """
        nameList = []
        for i in range(0, listSize):
            nameList.append(self.getUniqueName(itemLength[i]))
        return nameList

    def verifyTextContains(self, actualText, expectedText):
        """
        Verify actual text contains expected string
        :param actualText:
        :param expectedText:
        :return:
        """
        self.log.info("Actual text from application web UI : " + actualText)
        self.log.info("Expected text from application web UI : " + expectedText)
        if expectedText.lower() in actualText.lower():
            self.log.info("## VERIFICATION CONTAINS...!!!")
            return True
        else:
            self.log.info("## VERIFICATION DOES NOT CONTAINS...!")
            return False

    def verifyTextMatch(self, actualText, expectedText):
        """
        Verify Text Match

        :param actualText:
        :param expectedText:
        :return:
        """
        self.log.info("Actual text from application web UI : " + actualText)
        self.log.info("Expected text from application web UI : " + expectedText)
        if expectedText.lower() == actualText.lower():
            self.log.info("## VERIFICATION MATCHED...!!!")
            return True
        else:
            self.log.info("## VERIFICATION DOES NOT MATCHED...!")
            return False

    def verifyListMatch(self, expectedList, actualList):
        """
        Verify two list matches

        :param expectedList:
        :param actualList:
        :return:
        """
        return set(expectedList) == set(actualList)

    def verifyListContains(self, expectedList, actualList):
        """
        Verify actual list contains elements of expected list

        :param expectedList:
        :param actualList:
        :return:
        """
        length = len(expectedList)
        for i in range(0, length):
            if expectedList[i] not in actualList:
                return False
        else:
            return True
