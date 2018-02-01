import logging
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from data import xpmsdata
from data import elements
from pyxpmsframework.XpmsBase import XpmsBaseClass
from selenium.webdriver.remote.remote_connection import LOGGER

class ConfigurationSource(XpmsBaseClass):
    def __init__(self,driver):
        super(ConfigurationSource, self).__init__(driver)
        LOGGER.setLevel(logging.WARNING)
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

    #@pytest.allure.step('Clicking On Upload Button ')
    def Upload(self):
        self.pause()
        self.logger.info('Clicking on upload Field ')
        self.click(elements.IngestFileUploadEle)

    #@pytest.allure.step('Entering File in Ingest Field')
    def IngestFile(self,filepath):
        self.logger.info('Entering File Path Into Ingest Browse Field ',filepath)
        self.pause()
        self.enterFileInputText(elements.IngestFileBrowseEle,filepath)

    #@pytest.allure.step('Clicking On Source Links Under Configuration')
    def SelectSource(self):
        if not (self.isElementVisible(elements.SourceEle)):
            self.click(elements.ConfigurationEle)
            self.click(elements.SourceEle)
