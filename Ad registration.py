from oauth2client.service_account import ServiceAccountCredentials
import gspread
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time
from tkinter import *
import pandas
from bs4 import BeautifulSoup
import requests
import Architecture_done as ad
import random
import glob
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import get_img
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
import os
import json
import pyautogui
import logging
import Data_base as db
from selenium.webdriver.support.ui import WebDriverWait as wait


def serve_web_control():  # 웹 컨트롤
    wait(driver, 10).until(driver.get("https://member.serve.co.kr/login/login.asp?TargetPage=http://www.serve.co.kr/agency/agreement/service_agree.asp"))
    finder_name_send_key('txtUserID', "a01084851005")
    finder_name_send_key('pwdPassWord', "0738asdf")
    wait(driver, 10).until(driver.get(finder_class_click('btn_login')))
    wait(driver, 10).until(driver.get(finder_xpath_click('//*[@id="content"]/div[1]/div[1]/div[1]/div[1]/div[2]/ul/li[4]/a')))


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


def normal_information_radio(transaction_type):
    if transaction_type == '매매':
        return '//*[@id="price_kind1"]'
    elif transaction_type == '전세':
        return '//*[@id="price_kind2"]'
    elif transaction_type == '월세':
        return '//*[@id="price_kind3"]'
    elif transaction_type == '단기임대':
        return '//*[@id="price_kind4"]'
    else:
        print('기본정보라디오버튼실패')


def select_option(element_text):
    xpath = '//select[@id="space_seq"]//option[contains(text(),' + element_text + ')]'
    option = driver.find_element_by_xpath(xpath)
    option_data = option.text
    return option_data


def finder_partial_link_text_click(searching_for_text):
    link = driver.find_element_by_partial_link_text(searching_for_text)
    link.click()


scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'credentials.json', scope)

gc = gspread.authorize(credentials)
gc1 = gc.open('Restate stocks')
gc2 = gc1.worksheet('매물등록창')

saleCategory = gc2.acell('C2').value

print(saleCategory)  # 엑셀 데이터

address_by_road = '중동로 204'
city_of_address = '경기도 부천시'
style_of_building = '아파트'
part_of_register = '전유부'
dong_apt = '1309동'
ho_apt = '905호'
city = "부천시"
town = '중동'
apt_name = '그린타운삼성,우성'
first_step_category = "아파트"
sec_step_category = "아파트"
payment_method = "매매"
price_of_selling = '60000'
monthly_price = ''
province = "경기도"


# 건축물대장 발급

driver = webdriver.Chrome('chromedriver.exe')
time.sleep(1)
ad.web_control()
ad.web_login_gov()

wait(driver, 10).until(driver.get(
    ad.issue_architecture_register(address_by_road, city_of_address, style_of_building, part_of_register,
                                              dong_apt, ho_apt)))

# 매물분류 선택
owner_data = ad.get_owner_data()
owner_name = owner_data[0]  # 소유자 이름
owner_address = owner_data[1]  # 소유자 현등록주소
private_size = owner_data[2]  # 전용면적 사이즈
official_price = owner_data[3]  # 공공주택가격
orel = '본인'

serve_web_control()
wait(driver, 10).until(driver.get(
    selector('category1', first_step_category)))
time.sleep(0.1)
selector('category2', sec_step_category)
time.sleep(0.1)
finder_xpath_click(normal_information_radio(payment_method))
time.sleep(0.1)
selector('lcode_si', province)
time.sleep(0.1)
selector('lcode_gu', city)
time.sleep(0.1)
selector('lcode_dong', town)
time.sleep(0.1)
selector('complex_seq', apt_name)
time.sleep(0.5)

selector('space_seq', str(select_option(private_size)))
wait(driver, 10).until(driver.get(
    finder_name_send_key('price1', price_of_selling)))
try:
    finder_name_send_key('price2', monthly_price)

except:
    print('월세가 없습니다.')
finder_name_send_key('dong', dong_apt.replace('동', ''))
finder_name_send_key('ho', ho_apt.replace('호', ''))
finder_name_send_key('floor1', int(int(ho_apt.replace('호', '')) / 100))  # 층입력
finder_xpath_click('//*[@id="floorType1"]')  # 직접입력
finder_xpath_click('//*[@id="consultYN"]')  # 협의가능
finder_name_send_key('feature', 'tes')  # 제목
finder_name_send_key('good_desc', 't')  # 내용
finder_xpath_click('//*[@id="pay_cnt"]/tr[1]/td[2]/label')  # 쿠폰클릭
finder_name_send_key('goods_owner', owner_name)  # 소유자이름
finder_name_send_key('orel', orel)  # 본인체크
finder_xpath_click('//*[@id="agreeNaver"]')  # 동의체크
finder_xpath_click('//*[@id="btnend"]')  # 등록버튼
time.sleep(2)
finder_xpath_click('//*[@id="wrapBtn1"]/a')  # 홍보확인서 버튼클릭
time.sleep(4)
print(driver.title)


get_img.get_an_image(owner_name)
driver.switch_to.window(driver.window_handles[-1])  # 새창인식
print(driver.title)

time.sleep(3)










driver.switch_to.frame('sign1')

sign_canvas = driver.find_element_by_class_name('jSignature')
img0 = np.array(Image.open('out0.png').convert("1"))
mouse_position0 = np.argwhere(img0)


for x, y in mouse_position0:
    hover = ActionChains(driver).move_to_element_with_offset(sign_canvas, y*5, x*5)
    hover.click().perform()

time.sleep(1)

driver.switch_to.default_content()



driver.switch_to.frame('sign2')

sign_canvas2 = driver.find_element_by_class_name('jSignature')
img1 = np.array(Image.open('out1.png').convert("1"))
mouse_position1 = np.argwhere(img1)

for x, y in mouse_position1:
    hover = ActionChains(driver).move_to_element_with_offset(sign_canvas2, y*4, x*4)
    hover.click().perform()


time.sleep(1)
driver.switch_to.default_content()






driver.switch_to.frame('sign3')

sign_canvas3 = driver.find_element_by_class_name('jSignature')
img2 = np.array(Image.open('out2.png').convert("1"))
mouse_position2 = np.argwhere(img2)

for x, y in mouse_position2:
    hover = ActionChains(driver).move_to_element_with_offset(sign_canvas3, y*4, x*4)
    hover.click().perform()


time.sleep(1)
driver.switch_to.default_content()




print('성공')

