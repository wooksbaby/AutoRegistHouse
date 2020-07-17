import time
from selenium.webdriver.chrome.options import Options
import gspread
import numpy as np
from PIL import Image
from selenium.webdriver.support import expected_conditions as EC
from oauth2client.service_account import ServiceAccountCredentials
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
import Architecture_done as ad
import re
import get_img
from selenium.common.exceptions import TimeoutException

options = Options()
options.headless = True
driver = webdriver.Chrome('chromedriver.exe',options=options)
driver.implicitly_wait(30)

