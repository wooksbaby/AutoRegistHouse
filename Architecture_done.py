import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

options = Options()
options.headless = True
driver = webdriver.Chrome('chromedriver.exe')#, options=options)
driver.implicitly_wait(30)


def register_seg(register_segment):
    if register_segment == '주택':
        return '//*[@id="건축물관리대장발급신청서_IN-건축물관리대장발급신청서_입력항목_공통항목_대장구분_.라디오코드1"]'
    elif register_segment == '아파트':
        return '//*[@id="건축물관리대장발급신청서_IN-건축물관리대장발급신청서_입력항목_공통항목_대장구분_.라디오코드2"]'
    else:
        print('대장구분에러')


def register_type(register_types):
    if register_types == '총괄':
        return '//*[@id="건축물관리대장발급신청서_IN-건축물관리대장발급신청서_입력항목_공통항목_대장종류_.라디오코드11"]'
    elif register_types == '표제부':
        return '//*[@id="건축물관리대장발급신청서_IN-건축물관리대장발급신청서_입력항목_공통항목_대장종류_.라디오코드12"]'
    elif register_types == '전유부':
        return '//*[@id="건축물관리대장발급신청서_IN-건축물관리대장발급신청서_입력항목_공통항목_대장종류_.라디오코드13"]'
    else:
        print('대장종류에러')


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


def web_control():  # 웹 컨트롤
    driver.get("https://www.gov.kr/main?a=AA020InfoCappViewApp&CappBizCD=15000000098&HighCtgCD=A02004002&Mcode=10205")
    try:
        finder_partial_link_text_click('신청하기')

    except:
        print('신청하기')


def web_login_gov():  # 웹 로그인
    try:
        finder_partial_link_text_click('회원 신청하기')
    except:
        print('회원신청하기 없어짐')
    try:
        finder_partial_link_text_click('아이디')
    except:
        print('아이디란클릭하기실패')
    finder_name_send_key('userId', 'crimsonsky')  # 로그인 아이디 입력
    finder_name_send_key('pwd', "0801sap!@#")
    finder_xpath_click('//*[@id="genLogin"]')
    finder_xpath_click('/html/body/div[4]/div/div/p[2]/span[2]/a')  # 나중에변경하기


def issue_architecture_register(address_road, bunji_address, name_of_selling, city_address, style_building,
                                part_register, dong, ho):  # 건축물대장 발급받기
    finder_xpath_click('/html/body/div[5]/div/div[1]/div[1]/a[2]')  # 건축물대장 발급 들어가기
    finder_xpath_click('//*[@id="주소검색"]')  # 주소검색
    driver.switch_to.window(driver.window_handles[-1])
    finder_name_send_key('txtRoad', address_road)  # 주소 검색창 도로명주소 입력
    finder_xpath_click('//*[@id="frm_popup"]/fieldset/div/div/span/button')  # 주소 검색창 검색키 클릭
    time.sleep(4)
    try:
        finder_partial_link_text_click(name_of_selling)
    except:
        finder_partial_link_text_click(bunji_address)
    part_office = driver.find_element_by_xpath('//*[@id="frm_popup"]/fieldset/div[2]/div[3]')  # 주소 검색 행정기관 입력
    office = part_office.find_element_by_partial_link_text(city_address)
    office.click()
    driver.switch_to.window(driver.window_handles[0])
    finder_xpath_click('//*[@id="건축물관리대장발급신청서_IN-건축물관리대장발급신청서_입력항목_공통항목_대장구분_.라디오코드2"]')
    finder_xpath_click(register_seg(style_building))  # 대장구분입력
    if part_register == '아파트':
        register_category = '전유부'
    finder_xpath_click(register_type(register_category))  # 대장종류입력
    finder_xpath_click('//*[@id="btn_end"]')  # 민원신청하기 클릭
    time.sleep(9)
    driver.switch_to.window(driver.window_handles[-1])  # 새창인식
    finder_partial_link_text_click(dong)  # 아파트 동 입력
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[0])  # 기존창 복귀
    finder_xpath_click('//*[@id="btn_end"]')  # 민원신청하기 클릭
    time.sleep(9)
    driver.switch_to.window(driver.window_handles[-1])  # 새창인식
    finder_partial_link_text_click(ho)  # 아파트 호 입력
    time.sleep(8)
    driver.switch_to.window(driver.window_handles[0])  # 기존창 복귀
    time.sleep(4)
    finder_xpath_click('//*[@id="btn_end"]')  # 민원신청하기 클릭
    time.sleep(18)
    y = driver.find_element_by_partial_link_text('열람문서')  # 열람문서 클릭
    y.click()
    time.sleep(2)


def get_owner_data():
    time.sleep(7)
    driver.switch_to.window(driver.window_handles[-1])  # 새창인식
    time.sleep(3)

    owner_name = driver.find_element_by_xpath('//*[@id="main"]/tbody/tr[5]/td[6]').text  # 이름가져오기

    building_size = driver.find_element_by_xpath('//*[@id="main"]/tbody/tr[5]/td[5]').text  # 빌딩 사이즈

    owner_address = driver.find_element_by_xpath('//*[@id="main"]/tbody/tr[5]/td[7]').text  # 소유자 주소

    building_price = driver.find_element_by_xpath(
        '//*[@id="EncryptionAreaID_0"]/div/table[4]/tbody/tr[4]/td[7]').text  # 공동주택 가격

    owner_data = [owner_name, owner_address, building_size, building_price]
    driver.close()
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[0])

    return owner_data
# 동호수 받아오기
