from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
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
import re
import get_img
from selenium.common.exceptions import TimeoutException
import csv

# from selenium.webdriver.support import Select
import time


def selector(select_box_name, option):
    select = Select(driver.find_element_by_name(str(select_box_name)))
    select.select_by_visible_text(option)


def finder_name_send_key(name_address, contents):
    name = driver.find_element_by_name(name_address)
    name.send_keys(contents)


def finder_class_click(class_add):
    login_box = driver.find_element_by_class_name(class_add)
    login_box.click()


def finder_xpath_click(xpath_add):
    enroll_box = driver.find_element_by_xpath(xpath_add)
    enroll_box.click()


options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
options.headless = True
driver = webdriver.Chrome('chromedriver.exe', options=options)
driver.implicitly_wait(30)
driver.get(
    "https://member.serve.co.kr/login/login.asp?TargetPage=http://www.serve.co.kr/agency/agreement/service_agree.asp")
time.sleep(1)
finder_name_send_key('txtUserID', "a01084851005")
finder_name_send_key('pwdPassWord', "0738asdf")
finder_class_click('btn_login')
time.sleep(1)
finder_xpath_click('//*[@id="content"]/div[1]/div[1]/div[1]/div[1]/div[2]/ul/li[4]/a')
time.sleep(1)

print("opening chorome....")

csvData = ['Year', 'Make', 'Model', 'Body', 'Submodel', 'Size']

# variables
lcode_si = []
lcode_gu = []
lcode_dong = []
complex_seq = []
# zzzzzzzzzzzz = []
# dddddddddddddddddd = []
Yindex = Mkindex = Mdindex = Bdindex = 0  # Smindex = Sindex = 0

print("waiting for program to set variables....")
driver.implicitly_wait(30)

print("initializing and setting variables....")

# initializing si
si = driver.find_element_by_id("lcode_si")
si_text = si.text.split('\n')
si_select = Select(si)
si_select.select_by_index(1)
time.sleep(0.5)
# initializing gu
gu = driver.find_element_by_id("lcode_gu")
gu_text = gu.text.split('\n')
gu_select = Select(gu)
gu_select.select_by_index(1)
time.sleep(0.5)
# initializing dong
dong = driver.find_element_by_id("lcode_dong")
dong_text = dong.text.split('\n')
dong_select = Select(dong)
dong_select.select_by_index(1)
time.sleep(0.5)
seq = driver.find_element_by_id("complex_seq")
seq_text = seq.text

for si_index in si_text[1::]:
    si = driver.find_element_by_id("lcode_si")
    si_select = Select(si)
    si_select.select_by_visible_text(si_index)
    print(si_index)
    time.sleep(0.5)
    gu = driver.find_element_by_id("lcode_gu")
    gu_text = gu.text.split('\n')
    gu_select = Select(gu)
    for gu_index in gu_text[1::]:
        gu = driver.find_element_by_id("lcode_gu")
        print(gu_index)
        gu_select = Select(gu)
        gu_select.select_by_visible_text(gu_index)
        time.sleep(0.5)
        dong = driver.find_element_by_id("lcode_dong")
        dong_text = dong.text.split('\n')
        dong_select = Select(dong)
        for dong_index in dong_text[1::]:
            dong = driver.find_element_by_id("lcode_dong")
            print(dong_index)
            dong_select = Select(dong)
            dong_select.select_by_visible_text(dong_index)
            time.sleep(0.3)

            seq = driver.find_element_by_id("complex_seq")
            seq_select = Select(seq)
            seq_text = seq.text.split('\n')
            print(seq_text)
