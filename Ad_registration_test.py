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


suplly_space_py = 0
suplly_space_m2 = ""

def serve_web_control():  # 웹 컨트롤

    driver.get("https://member.serve.co.kr/login/login.asp?TargetPage=http://www.serve.co.kr/agency/agreement/service_agree.asp")
    time.sleep(1)
    finder_name_send_key('txtUserID', "a01084851005")
    finder_name_send_key('pwdPassWord', "0738asdf")
    finder_class_click('btn_login')
    time.sleep(1)
    finder_xpath_click('//*[@id="content"]/div[1]/div[1]/div[1]/div[1]/div[2]/ul/li[4]/a')
    time.sleep(1)
    print('성공')


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


def select_option(first_step_category, sec_step_category, payment_method, province, city, town, apt_name,
                  price_of_selling, monthly_price, dong_apt, ho_apt, owner_name, private_size_test, orel):
    # 매물분류 선택

    selector('category1', first_step_category)
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
    xpath = '//select[@id="space_seq"]//option[contains(text(),' + private_size_test + ')]'
    driver.find_element_by_xpath(xpath).click()
    global suplly_space_py
    global suplly_space_m2
    suplly_space_raw = driver.find_element_by_xpath(xpath).text
    suplly_space_index1 = suplly_space_raw.find('(') + 1
    suplly_space_index2 = suplly_space_raw.find(')')
    suplly_space_m2 = suplly_space_raw[suplly_space_index1:suplly_space_index2]
    suplly_space_float = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", suplly_space_m2)[0]
    suplly_space_py = round(float(suplly_space_float) * 0.3025)
    time.sleep(1)
    finder_name_send_key('price1', int(price_of_selling))

    try:
        finder_name_send_key('price2', int(monthly_price))

    except:
        print('매매나 전세입니다.')
    time.sleep(1)
    finder_name_send_key('dong', dong_apt.replace('동', ''))
    finder_name_send_key('ho', ho_apt.replace('호', ''))
    finder_name_send_key('floor1', int(int(ho_apt.replace('호', '')) / 100))  # 층입력
    finder_xpath_click('//*[@id="floorType1"]')  # 직접입력
    finder_xpath_click('//*[@id="consultYN"]')  # 협의가능
    title_of_advertisement = str('확인한매물.' + str(suplly_space_py) + ',' + str(suplly_space_m2) + '㎡ ' + '협의' + '깨끗한집')
    contents_of_advertisement = "정직한 부동산 부동산랜드입니다.\n", "부동산 거래에 문제가 있나요? 부동산 거래 잘모르겠나요? 답답한문제가 있나요?\n", "모든 걱정되는 문제 모를수있는 문제 성실히 해결해 드리겠습니다.\n", "비교해보실수 있는 매물 다량 보유하고있습니다.\n\n",'"좋은집 구하는 제일 좋은 방법은 인터넷이 아닌 전화 한통입니다."\n\n', '032)322-0511, 010)8485-1005'

    finder_name_send_key('feature', title_of_advertisement)  # 제목
    finder_name_send_key('good_desc', contents_of_advertisement)  # 내용
    finder_xpath_click('//*[@id="pay_cnt"]/tr[1]/td[2]/label')  # 쿠폰클릭
    finder_name_send_key('goods_owner', owner_name)  # 소유자이름
    finder_name_send_key('orel', orel)  # 본인체크
    finder_xpath_click('//*[@id="agreeNaver"]')  # 동의체크
    finder_xpath_click('//*[@id="btnend"]')  # 등록버튼
    time.sleep(2)
    finder_xpath_click('//*[@id="wrapBtn1"]/a')  # 홍보확인서 버튼클릭
    time.sleep(2)
    get_img.get_an_image(owner_name)
    driver.switch_to.window(driver.window_handles[-1])  # 새창인식
    time.sleep(1)

    wait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it("sign1"))

    sign_canvas = driver.find_element_by_class_name('jSignature')
    img0 = np.array(Image.open('out0.png').convert("1"))
    mouse_position0 = np.argwhere(img0)

    for x, y in mouse_position0:
        hover = ActionChains(driver).move_to_element_with_offset(sign_canvas, y * 5, x * 5)
        hover.click().perform()

    time.sleep(1)
    elem = driver.find_element_by_tag_name("body")
    elem.send_keys(Keys.PAGE_DOWN)
    driver.switch_to.default_content()
    wait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it("sign2"))

    sign_canvas2 = driver.find_element_by_class_name('jSignature')
    img1 = np.array(Image.open('out1.png').convert("1"))
    mouse_position1 = np.argwhere(img1)

    for x, y in mouse_position1:
        hover = ActionChains(driver).move_to_element_with_offset(sign_canvas2, y * 4, x * 4)
        hover.click().perform()

    time.sleep(1)
    driver.switch_to.default_content()
    wait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it("sign3"))

    sign_canvas3 = driver.find_element_by_class_name('jSignature')
    img2 = np.array(Image.open('out2.png').convert("1"))
    mouse_position2 = np.argwhere(img2)

    for x, y in mouse_position2:
        hover = ActionChains(driver).move_to_element_with_offset(sign_canvas3, y * 4, x * 4)
        hover.click().perform()
    time.sleep(1)

    driver.switch_to.default_content()
    wait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it("workFrame"))
    finder_class_click('btn_ok')
    driver.switch_to.default_content()
    time.sleep(1)
    time.sleep(1)
    finder_xpath_click('//*[@id="btn_cap_1"]/a[2]')
    time.sleep(1)
    try:
        wait(driver, 3).until(EC.alert_is_present(),
                              'Timed out waiting for PA creation ' + 'confirmation popup to appear.')
        alert = driver.switch_to.alert
        alert.accept()
        print("alert accepted")

    except TimeoutException:
        print("no alert")

    driver.switch_to.default_content()
    time.sleep(3)
    finder_xpath_click('/html/body/div[2]/div/a')

    time.sleep(3)
    driver.switch_to.window(driver.window_handles[0])
    finder_xpath_click('//*[@id="wrapBtn1"]/a[3]')


def resister_continue():
    driver.get('http://www.serve.co.kr/agency/maemul/nmaemul_reg.asp')
    time.sleep(3)