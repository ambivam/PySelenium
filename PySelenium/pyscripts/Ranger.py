
import pytest
import time
from selenium import webdriver
from data import xpmsdata
from data import elements
from data import inputdata
from configuration.ExcelReading import ExcelOperations
import os
import json
import logging
import allure
from pyxpmsframework.XpmsBase import XpmsBaseClass
from pyxpmsframework.LoginPage import Login
from pyxpmsframework.UserManagementPage import UserManagement


#*****************************************************************
driver = None
logger = logging.getLogger(__name__)
excelOperations = ExcelOperations()
#*****************************************************************
def setup_function(function):
    global driver
    driver = XpmsBaseClass.getBrowser('chrome')
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
#****************************************************************
def teardown_function(function):
    XpmsBaseClass().pause()
    global driver
    driver.quit()
    driver.close()


#*****************************************************************
@pytest.allure.step('To Test The Login Functionality ,Verifying admin Welcome Text and Logging out of admin page')
@allure.story('Smoke','TC01_LoginAndLogoutUserAdminPage')
def test_AdminLogin():
    tempResult = False
    username = excelOperations.getExcelData("TC01","UserName")
    password = excelOperations.getExcelData("TC01","Password")
    adminWelcomeText = excelOperations.getExcelData("TC01","AdminWCText")
    loginText = excelOperations.getExcelData("TC01","LoginText")
    url = excelOperations.getExcelData("TC01","RangerURL")
    #filePathJson = os.path.abspath(__file__ + "/../../data/jsonfiles") + '/'
    #filePathImages = os.path.abspath(__file__ + "/../../data/images") + '/'+inputdata.Image1
    #*************************************************************
    with pytest.allure.step('Opening The Browser with URL : '+url):
        driver.get(url)
    #*************************************************************
    loginDriver = Login(driver)
    # *************************************************************
    with pytest.allure.step('Logging Into Admin Page using username:'+username+', password :' +password ):
        loginDriver.login(username,password)
        usermanagementdriver = UserManagement(driver)
    # *************************************************************
    with pytest.allure.step('Verifying user is able to view :'+adminWelcomeText ):
        tempResult = usermanagementdriver.verifyWelcomeText(adminWelcomeText)
        if(tempResult):
            with pytest.allure.step('User is able to view :' + adminWelcomeText):
                logger.info('User is able to view :' + adminWelcomeText)
        else:
            with pytest.allure.step('User is unable to view :' + adminWelcomeText):
                logger.error('User is unable to view :' + adminWelcomeText)
            usermanagementdriver.takeScreenShot()
    # *************************************************************
    with pytest.allure.step('Logging Out From Admin page'):

        usermanagementdriver.logout()
        tempResult = loginDriver.verifyLoginText(loginText)
        if(tempResult):
            with pytest.allure.step('Login text is displayed,hence verified User is successfully logged out of User admin page'):
                logger.info('Login text is displayed,hence verified User is successfully logged out of User admin page')
        else:
            with pytest.allure.step('Login text is not displayed,hence verified User is not successfully logged out of User admin page'):
                logger.error('Login text is not displayed,hence verified User is not successfully logged out of User admin page')
            usermanagementdriver.takeScreenShot()
    # *************************************************************

#*****************************************************************

#*****************************************************************
@pytest.allure.step('To Test The Login Functionality ,Verifying admin Welcome Text and Logging out of admin page using Invalid Creds')
@allure.story('Smoke','TC02_LoginAndLogoutUserAdminPageNegative')
def test_AdminLoginInvalidCreds():
    tempResult = False
    username = excelOperations.getExcelData("TC02","UserName")
    password = excelOperations.getExcelData("TC02","Password")
    adminWelcomeText = excelOperations.getExcelData("TC02","AdminWCText")
    loginText = excelOperations.getExcelData("TC02","LoginText")
    url = excelOperations.getExcelData("TC02", "RangerURL")
    #filePathJson = os.path.abspath(__file__ + "/../../data/jsonfiles") + '/'
    #filePathImages = os.path.abspath(__file__ + "/../../data/images") + '/'+inputdata.Image1
    #*************************************************************
    with pytest.allure.step('Opening The Browser with URL : '+url):
        driver.get(url)
    #*************************************************************
    loginDriver = Login(driver)
    # *************************************************************
    with pytest.allure.step('Logging Into Admin Page using invalid username:'+username+', invalid password :' +password ):
        loginDriver.login(username,password)
        #usermanagementdriver = UserManagement(driver)
    # *************************************************************
    # *************************************************************
    with pytest.allure.step('Verifying user is still on the Login page :'):

        #usermanagementdriver.logout()
        tempResult = loginDriver.verifyLoginText(loginText)
        if(tempResult):
            with pytest.allure.step('Login text is displayed,hence verified User is did not logged into User admin page'):
                logger.info('Login text is displayed,hence verified User is did not logged into User admin page')
        else:
            with pytest.allure.step('Login text is not displayed,hence verified User logged into User admin page'):
                logger.error('Login text is not displayed,hence verified User logged into User admin page')
            loginDriver.takeScreenShot()
    # *************************************************************

#*****************************************************************







