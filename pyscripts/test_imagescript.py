
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
from pyxpmsframework.DashboardPage import Dashboard
from pyxpmsframework.ConfigurationSourcePage import ConfigurationSource

#*****************************************************************
driver = None
#*****************************************************************
def setup_function(function):
    global driver
    driver = XpmsBaseClass.getBrowser('chrome')
#*****************************************************************
def teardown_function(function):
    driver.quit()
#*****************************************************************

def test_numbers_3_4():
    filePathJson = os.path.abspath(__file__ + "/../../data/jsonfiles") + '/'
    filePathImages = os.path.abspath(__file__ + "/../../data/images") + '/'+inputdata.Image1
    with pytest.allure.step('Opening The Browser'):
        driver.get('http://uat.intake.xpms.ai')
    logindriver = Login(driver)
    logindriver.login(inputdata.username,inputdata.password)

    with pytest.allure.step('Opening The Browser {0}'):
        dashboard = Dashboard(logindriver.getDriver())
        dashboard.showing(inputdata.showing)

    sourcedriver = ConfigurationSource(dashboard.getDriver())
    sourcedriver.SelectSource()
    sourcedriver.IngestFile(filePathImages)
    sourcedriver.Upload()
    sourcedriver.takeScreenShot()
    sourcedriver.pause()
    dashboard.SelectDashboard()
    sourcedriver.pause()
    dashboard.search(inputdata.image)
    dashboard.takeScreenShot()
    dashboard.pause()
#*****************************************************************






