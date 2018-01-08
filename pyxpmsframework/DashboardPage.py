import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from data import xpmsdata
from data import elements

from pyxpmsframework.XpmsBase import XpmsBaseClass
from selenium.webdriver.remote.remote_connection import LOGGER

class Dashboard(XpmsBaseClass):
    def __init__(self,driver):
        super(Dashboard, self).__init__(driver)
        LOGGER.setLevel(logging.WARNING)
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

    def showing(self,period):
        self.logger.info('In Showing Selecting '+period)
        self.selectText(elements.ShowingEle,period)

    def enterSearchText(self,searchText):
        self.logger.info('Entering Search text :'+searchText)
        self.enterText(elements.SearchTextFieldEle,searchText)

    def clickSearch(self):
        self.logger.info('Clicking on Search button')
        self.click(elements.SearchButtonEle)

    def search(self,searchText):
        self.logger.info('Performing Search of : '+ searchText)
        self.enterSearchText(searchText)
        self.clickSearch()
        self.pause()

    def SelectDashboard(self):
        self.logger.info('Clicking On Dashboard Link ')
        self.click(elements.DashboardLinkEle)



