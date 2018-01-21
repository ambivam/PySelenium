import pytest
import time
from selenium import webdriver
from data import xpmsdata
from data import elements
from data import inputdata
from configuration.ExcelReading import ExcelOperations
from selenium.webdriver.remote.command import Command
import os
import json
import logging
import allure
from pyxpmsframework.XpmsBase import XpmsBaseClass
from pyxpmsframework.LoginPage import Login
from pyxpmsframework.UserManagementPage import UserManagement


#*****************************************************************
class TestLogin:


    driver = None
    excelOperations = ExcelOperations()
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)


    def setup_method(self):
        self.logger.info("Initializing the driver")
        if(self.driver == None):
            self.driver = XpmsBaseClass.getBrowser('chrome')
            self.logger.info("Driver Initialized")
        self.logger.info("$$$$$$$$$$$$$ INTO SETUP METHOD $$$$$$$$$$$$$$$$$")


    def teardown_method(self):
        self.logger.info("$$$$$$$$$$$$$ INTO TEARDOWN METHOD $$$$$$$$$$$$$$$$$")
        try:
            self.logger.info("Closing The driver")
            if (self.driver.session_id is not None):
                self.logger.info('The Command status is 0')
                #self.driver.close()
                self.driver.quit()
                #self.driver.session_id = None
                self.logger.info("Driver is closed")
        except:
            self.logger.info("exception generated when accessing driver object while quitting it")


    @pytest.allure.step('To Test The Login Functionality ,Verifying admin Welcome Text and Logging out of admin page')
    @allure.story('Smoke','TC01_LoginAndLogoutUserAdminPage')
    def test_adminLogin(self):
        tempResult = False
        username = self.excelOperations.getExcelData("TC01", "UserName")
        password = self.excelOperations.getExcelData("TC01", "Password")
        adminWelcomeText = self.excelOperations.getExcelData("TC01", "AdminWCText")
        loginText = self.excelOperations.getExcelData("TC01", "LoginText")
        url = self.excelOperations.getExcelData("TC01", "RangerURL")
        # *************************************************************
        with pytest.allure.step('Opening The Browser with URL : ' + url):
            self.driver.get(url)
        # *************************************************************
        loginDriver = Login(self.driver)
        # *************************************************************
        with pytest.allure.step('Logging Into Admin Page using username:' + username + ', password :' + password):
            loginDriver.login(username, password)
            usermanagementdriver = UserManagement(self.driver)
        # *************************************************************
        with pytest.allure.step('Verifying user is able to view :' + adminWelcomeText):
            tempResult = usermanagementdriver.verifyWelcomeText(adminWelcomeText)
            if (tempResult):
                with pytest.allure.step('User is able to view :' + adminWelcomeText):
                    self.logger.info('User is able to view :' + adminWelcomeText)
            else:
                with pytest.allure.step('User is unable to view :' + adminWelcomeText):
                    self.logger.error('User is unable to view :' + adminWelcomeText)
                usermanagementdriver.takeScreenShot()
        # *************************************************************
        with pytest.allure.step('Logging Out From Admin page'):

            usermanagementdriver.logout()
            tempResult = loginDriver.verifyLoginText(loginText)
            if (tempResult):
                with pytest.allure.step('Login text is displayed,hence verified User is successfully logged out of User admin page'):
                    self.logger.info(
                        'Login text is displayed,hence verified User is successfully logged out of User admin page')
            else:
                with pytest.allure.step('Login text is not displayed,hence verified User is not successfully logged out of User admin page'):
                    self.logger.error(
                        'Login text is not displayed,hence verified User is not successfully logged out of User admin page')
                    loginDriver.takeScreenShot()
            #XpmsBaseClass().pause()
            #import pdb;pdb.set_trace()
        # *************************************************************

    #*****************************************************************

    #*****************************************************************
    @pytest.allure.step('To Test The Login Functionality ,Verifying admin Welcome Text and Logging out of admin page using Invalid Creds')
    @allure.story('Smoke','TC02_LoginAndLogoutUserAdminPageNegative')
    def test_adminLoginInvalidCreds(self):
        tempResult = False
        username = self.excelOperations.getExcelData("TC02","UserName")
        password = self.excelOperations.getExcelData("TC02","Password")
        adminWelcomeText = self.excelOperations.getExcelData("TC02","AdminWCText")
        loginText = self.excelOperations.getExcelData("TC02","LoginText")
        url = self.excelOperations.getExcelData("TC02", "RangerURL")
        #*************************************************************
        with pytest.allure.step('Opening The Browser with URL : '+url):
            #self.driver.get(url)
            self.driver.get(url)
        #*************************************************************
        loginDriver = Login(self.driver)
        # *************************************************************
        with pytest.allure.step('Logging Into Admin Page using invalid username:'+username+', invalid password :' +password ):
            loginDriver.login(username,password)
            #usermanagementdriver = UserManagement(driver)
        # *************************************************************
        # *************************************************************
        with pytest.allure.step('Verifying user is still on the Login page :'):

            #usermanagementdriver.logout()
            tempResult = loginDriver.verifyLoginText(loginText)
            if (tempResult):
                with pytest.allure.step('Login text is displayed,hence verified User is did not logged into User admin page'):
                    self.logger.info('Login text is displayed,hence verified User is did not logged into User admin page')
            else:
                with pytest.allure.step('Login text is not displayed,hence verified User logged into User admin page'):
                    self.logger.error('Login text is not displayed,hence verified User logged into User admin page')
                loginDriver.takeScreenShot()
            #XpmsBaseClass.pause()
        # *************************************************************



    #*****************************************************************








