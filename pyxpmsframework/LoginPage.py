import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from data import xpmsdata
from data import elements
from data import inputdata
from pyxpmsframework.DashboardPage import Dashboard
import allure
import pytest

from pyxpmsframework.XpmsBase import XpmsBaseClass
from selenium.webdriver.remote.remote_connection import LOGGER

class Login(XpmsBaseClass):

    def __init__(self,driver):
        LOGGER.setLevel(logging.WARNING)
        self.driver = driver
        super(Login, self).__init__(self.driver)
        self.logger = logging.getLogger(__name__)

    @pytest.allure.step('Enter User Name username ')
    def enterUserName(self,username):
        #import  pdb;pdb.set_trace()
        self.logger.info('Enter User name :'+username)
        self.enterText(elements.UserNameEle,username)

    @allure.step('Enter Password ')
    def enterPassword(self,password):
        self.logger.info('Enter Password :'+password)
        self.enterText(elements.PasswordEle,password)

    @allure.step('Clicking On Sign Button Of Login')
    def clickSignIn(self):
        self.logger.info('Sign In clicked')
        self.click(elements.SignInEle)

    @allure.step('Logging Into Console Application ')
    def login(self,username,password):
        self.enterUserName(username)
        self.enterPassword(password)
        self.clickSignIn()
        self.pause()

    @allure.step('Verifying Login Text of Login Page ')
    def verifyLoginText(self, loginText):
        self.logger.info('Verifying Login text is displayed on Login Page ')
        return self.verifyText(elements.LoginEle, inputdata.loginText)