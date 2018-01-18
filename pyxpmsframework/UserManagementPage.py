import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from data import xpmsdata
from data import elements
from data import inputdata
import allure

from pyxpmsframework.XpmsBase import XpmsBaseClass
from selenium.webdriver.remote.remote_connection import LOGGER

class UserManagement(XpmsBaseClass):
    def __init__(self,driver):
        super(UserManagement, self).__init__(driver)
        LOGGER.setLevel(logging.WARNING)
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

    #*********************************************************
    @allure.step('Logging out of User Admin Page ')
    def logout(self):
        self.logger.info('Logging out from User Admin Page  ')
        self.click(elements.AdminLogoutAvatar)
        self.pause()
        self.click(elements.AdminLogout)
        self.pause()

    @allure.step('Verifying Welcome Text of User Admin Page ')
    def verifyWelcomeText(self,welcomeText):
        self.logger.info('Verifying Welcome to User Management Page is displayed  ')
        return self.verifyText(elements.AdminWelcomeText,inputdata.adminWelcomeText)




    #**********************************************************





