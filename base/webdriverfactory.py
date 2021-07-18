"""
@package base

Webdriver factory creates a webdriver instance based on browser configurations
"""
import logging
import os
import traceback
from selenium import webdriver
import utilities.custom_logger as cl


class WebDriverFactory():
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, browser):
        self.log.info("Inside Init of webdriver factory")
        """
        Inits webdriverfactory class
        return:
            None
        :param browser:
        """
        self.browser = browser

        # Set Chrome driver and IExplorer environment based on OS
        # Chromedriver = "path"

        # chromedriver = "drivers/chromedriver.exe"
        # os.environ["webdriver.chrome.driver"] = chromedriver
        # self.driver = webdriver.Chrome(chromedriver)

    def getWebDriverInstance(self):
        """
        Get webdriver instance based on browser configuration
        :return:
            webdriver instance
        """
        baseURL = "https://courses.letskodeit.com/"
        if self.browser == "iexplorer":
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            print("Launching a chrome browser")
            driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")
        # else:
        #     driver = webdriver.Chrome()
        # Setting driver implicit wait
        driver.implicitly_wait(10)
        # Maximize the window
        driver.maximize_window()
        # Loading URL
        driver.get(baseURL)
        return driver
