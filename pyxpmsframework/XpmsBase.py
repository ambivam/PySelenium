import logging
import os

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from data import xpmsdata
from datetime import datetime
from allure.constants import AttachmentType
from selenium.webdriver.remote.remote_connection import LOGGER
import time



class XpmsBaseClass(object):
    browserDrivers = {'chrome':None,'firefox':None}

    def __init__(self,selenium_driver):
        LOGGER.setLevel(logging.WARNING)
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        self.driver = selenium_driver
        self.driver.maximize_window()


    @staticmethod
    def getBrowser(browserName):
        if(str(browserName).lower() == 'chrome'):
            if(XpmsBaseClass.browserDrivers['chrome'] is None):
                filePath = os.path.abspath(__file__ + "/../../config/chromedriver")
                XpmsBaseClass.browserDrivers['chrome'] = webdriver.Chrome(filePath)
                return XpmsBaseClass.browserDrivers['chrome']
            else:
                return XpmsBaseClass.browserDrivers['chrome']
        elif(str(browserName).lower() == 'firefox'):
            if (XpmsBaseClass.browserDrivers['firefox'] is None):
                filePath = os.path.abspath(__file__ + "/../../config/firefoxdriver")
                XpmsBaseClass.browserDrivers['firefox'] = webdriver.Firefox(filePath)
                return XpmsBaseClass.browserDrivers['firefox']
            else:
                return XpmsBaseClass.browserDrivers['firefox']

    def getElement(self,element):
        temp = ''
        tempElement = None
        wait = WebDriverWait(self.driver, xpmsdata.timeout)

        if (element.lower().startswith('xpath')):
            temp = element.split('xpath_')[1]
            self.logger.info('performing action on an element using Xpath'+temp)
            tempElement = wait.until(EC.element_to_be_clickable((By.XPATH, temp)))
            #tempElement = self.driver.find_element_by_xpath(temp)
        elif (str(element).lower().startswith('id')):
            temp = element.split('id_')[1]
            self.logger.info('performing action on an element using Id' + temp)
            tempElement = wait.until(EC.element_to_be_clickable((By.ID, temp)))
        elif (str(element).lower().startswith('link')):
            temp = element.split('link_')[1]
            self.logger.info('performing action on an element using Link' + temp)
            tempElement = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, temp)))
        elif (str(element).lower().startswith('css')):
            temp = element.split('css_')[1]
            self.logger.info('performing action on an element using css' + temp)
            tempElement = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, temp)))
        elif (str(element).lower().startswith('name')):
            temp = element.split('name_')[1]
            self.logger.info('performing action on an element using Name' + temp)
            tempElement = wait.until(EC.element_to_be_clickable((By.NAME, temp)))
        elif (str(element).lower().startswith('tag')):
            temp = element.split('tag_')[1]
            self.logger.info('performing action on an element using Tag' + temp)
            tempElement = wait.until(EC.element_to_be_clickable((By.TAG_NAME, temp)))
        return tempElement

    def enterFileInputText(self,element,filepath):
        try:
            temp = element.split('xpath_')[1]
            self.pause()
            temEle = self.driver.find_element_by_xpath(temp)
            self.logger.info('Into enterFileInputtext method ')
            temEle.send_keys(str(filepath))
        except:
            self.logger.error('Unable To Enter into File Input text ' + filepath)
            self.raiseException()


    def click(self,element):
        try:
            temElement = self.getElement(element)
            self.logger.info('Into Click method ')
            temElement.click()
        except:
            self.logger.error('Unable To click on Element' )
            self.raiseException()

    def getText(self,element):
        try:
            temElement = self.getElement(element)
            self.logger.info('Into gettext method ')
            return temElement.text
        except:
            self.logger.error('Unable To retrieve the text from the element')
            self.raiseException()

    def verifyText(self,element,elementText):
        try:
            temElement = self.getElement(element)
            self.logger.info('Into gettext method ')
            if(str(temElement.text).lower() == str(elementText).lower()):
                return True
            else:
                return False
        except:
            self.logger.error('Unable To verify the text'+elementText)
            self.raiseException()


    def enterText(self,element,strText):
        try:
            temEle = self.getElement(element)
            self.logger.info('Into entertext method ')
            temEle.send_keys(str(strText))
        except:
            self.logger.error('Unable To Enter text ' + strText)
            self.raiseException()

    def selectText(self,element,strText):
        try:
            select = Select(self.getElement(element))
            self.logger.info('Into selectText method ')
            select.select_by_visible_text(strText)
        except:
            self.logger.error('Unable To select text '+strText)
            self.raiseException()

    def isElementVisible(self,element):
        result = False
        try:
            tempEle = self.getElement(element)
            result =tempEle.is_displayed()
        except:
            self.logger.info('Unable To Verify Visibility Of Element ')
        return result

    def takeScreenShot(self):
        self.logger.info('Taking Screenshot')
        allure.attach('Screenshot', self.driver.get_screenshot_as_png(), type=AttachmentType.PNG)


    def raiseException(self):
        self.takeScreenShot()
        self.cleanup()
        self.logger.error('Exception Raised')
        assert True == False

    def cleanup(self):
        self.logger.info('Closing Browser Instances')
        self.driver.quit()

    def pause(self):
        self.logger.info('Into pause')
        time.sleep(xpmsdata.sleepTime)

    def getDriver(self):
        self.logger.info('getting The Driver')
        return self.driver


