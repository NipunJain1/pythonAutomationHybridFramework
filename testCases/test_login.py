import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_login:
    URL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):

        self.logger.info("**********Start TC1***************")
        self.driver = setup
        self.driver.get(self.URL)
        title = self.driver.title

        if title != "":
            self.driver.close()
            self.logger.info("**********TC1 Pass***************")
            assert True
        else:
            self.logger.info("**********TC1 Fail***************")
            self.driver.save_screenshot(".\\Screenshots\\test_homePageTitle.png")
            self.driver.close()
            assert False

    def test_login(self, setup):
        self.logger.info("**********TC2 Starting***************")
        self.driver = setup
        self.driver.get(self.URL)

        self.lp = LoginPage(self.driver, self.username, self.password)
        self.lp.Login()

        title = self.driver.title
        if title == "Dashboard / nopCommerce administration":
            self.driver.close()
            self.logger.info("**********TC2 Pass***************")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_login.png")
            self.driver.close()
            self.logger.info("**********TC2 Fail***************")
            assert False
