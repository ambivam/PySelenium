import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from data import xpmsdata
from data import elements
from data import inputdata
import allure

from pyxpmsframework.XpmsBase import XpmsBaseClass
from pyxpmsframework.LoginPage import Login
from selenium.webdriver.remote.remote_connection import LOGGER

class Redirection(XpmsBaseClass):
    def __init__(self,driver):
        super(Redirection, self).__init__(driver)
        LOGGER.setLevel(logging.WARNING)
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

    def returnLogin(self):
        return Login(self.driver)

