import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select


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
    xpath = driver.find_element_by_xpath(xpath_add)
    xpath.click()


def finder_partial_link_text_click(searching_for_text):
    searching_text = driver.find_element_by_partial_link_text(searching_for_text)
    searching_text.click()




TEST_URL = "https://member.serve.co.kr/login/login.asp?TargetPage=http://www.serve.co.kr/agency/agreement/service_agree.asp"

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")

driver = webdriver.Chrome('chromedriver.exe', options=options)

driver.get(TEST_URL)

driver.get(
    "https://member.serve.co.kr/login/login.asp?TargetPage=http://www.serve.co.kr/agency/agreement/service_agree.asp")
time.sleep(1)
finder_name_send_key('txtUserID', "a01084851005")
finder_name_send_key('pwdPassWord', "0738asdf")
finder_class_click('btn_login')
time.sleep(1)
finder_xpath_click('//*[@id="content"]/div[1]/div[1]/div[1]/div[1]/div[2]/ul/li[4]/a')
time.sleep(1)

dropdown_elements_si = driver.find_elements_by_xpath("//select[@name='lcode_si']/option")
dropdown_elements_gu = driver.find_elements_by_xpath("//select[@name='lcode_gu']/option")
dropdown_elements_dong = driver.find_elements_by_xpath("//select[@name='lcode_dong']/option")
dropdown_elements_complex_seq = driver.find_elements_by_xpath("//select[@name='complex_seq']/option")
dropdown_elements_space_seq = driver.find_elements_by_xpath("//select[@name='space_seq']/option")

for element_si in dropdown_elements_si[1::]:
    Select(driver.find_element_by_name(str('lcode_si'))).select_by_visible_text(str(element_si.text))
    time.sleep(2)
    print(element_si.text)
    # time.sleep(0.1)
    # selector('lcode_gu', city)
    # time.sleep(0.1)
    # selector('lcode_dong', town)
    # time.sleep(0.1)
    # selector('complex_seq', apt_name)
    # time.sleep(0.5)
    #
















    # for element_gu in dropdown_elements_gu:
    #     print(element_gu.text)
    #     time.sleep(0.1)
    #     # for element_dong in dropdown_elements_dong:
    #     #     print(element_dong.text)
    #     #     for element_complex_seq in dropdown_elements_complex_seq:
    #     #         print(element_complex_seq.text)
    #     #         for element_space_seq in dropdown_elements_space_seq:
    #     #             print(element_space_seq.text)
    #     #





driver.quit()