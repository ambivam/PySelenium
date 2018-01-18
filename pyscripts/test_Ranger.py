
import pytest
import time
from selenium import webdriver
from data import xpmsdata
from data import elements
from data import inputdata
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
#*****************************************************************
def setup_function(function):
    global driver
    driver = XpmsBaseClass.getBrowser('chrome')
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
#*****************************************************************
def teardown_function(function):
    driver.quit()
#*****************************************************************
@pytest.allure.step('To Test The Login Functionality ,Verifying admin Welcome Text and Logging out of admin page')
@allure.story('Smoke','LoginAndLogoutUserAdminPage')
def test_AdminLogin():
    tempResult = False
    filePathJson = os.path.abspath(__file__ + "/../../data/jsonfiles") + '/'
    filePathImages = os.path.abspath(__file__ + "/../../data/images") + '/'+inputdata.Image1
    #*************************************************************
    with pytest.allure.step('Opening The Browser with URL : '+inputdata.rangerUrl):
        driver.get(inputdata.rangerUrl)
    #*************************************************************
    loginDriver = Login(driver)
    # *************************************************************
    with pytest.allure.step('Logging Into Admin Page using username:'+inputdata.username+', password :' +inputdata.password ):
        loginDriver.login(inputdata.username,inputdata.password)
        usermanagementdriver = UserManagement(driver)
    # *************************************************************
    with pytest.allure.step('Verifying user is able to view :'+inputdata.adminWelcomeText ):
        tempResult = usermanagementdriver.verifyWelcomeText(inputdata.adminWelcomeText)
        if(tempResult):
            with pytest.allure.step('User is able to view :' + inputdata.adminWelcomeText):
                logger.info('User is able to view :' + inputdata.adminWelcomeText)
        else:
            with pytest.allure.step('User is unable to view :' + inputdata.adminWelcomeText):
                logger.error('User is unable to view :' + inputdata.adminWelcomeText)
            usermanagementdriver.takeScreenShot()
    # *************************************************************
    with pytest.allure.step('Logging Out From Admin page'):

        usermanagementdriver.logout()
        tempResult = loginDriver.verifyLoginText(inputdata.loginText)
        if(tempResult):
            with pytest.allure.step('Login text is displayed,hence verified User is successfully logged out of User admin page'):
                logger.info('Login text is displayed,hence verified User is successfully logged out of User admin page')
        else:
            with pytest.allure.step('Login text is not displayed,hence verified User is not successfully logged out of User admin page'):
                logger.error('Login text is not displayed,hence verified User is not successfully logged out of User admin page')
            usermanagementdriver.takeScreenShot()
    # *************************************************************

#*****************************************************************






