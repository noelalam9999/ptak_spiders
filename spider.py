from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.firefox.options import Options
import sys
import bs4
from pywebcopy import save_webpage
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest, time, re
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from pyvirtualdisplay import Display

display = Display(visible=0, size=(1024,768))
display.start()
binary = FirefoxBinary('/opt/firefox60/firefox')
options = Options()
options.set_headless(headless=True)
options.binary = binary


cap = DesiredCapabilities.FIREFOX
cap['marionette'] = True
cap['binary']='opt/firefox60/firefox'
browser = webdriver.Firefox(firefox_options=options, capabilities=cap, executable_path="/usr/local/bin/geckodriver")
print("Headless Firefox Initialized")
browser.get("http://google.com/")
browser.quit()
display.stop()
