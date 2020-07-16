import Data_base as Db
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import Architecture_done as ad
import Ad_registration_test as ar
import time
import math

task_var = Db.task_variable
update_col = Db.start_row_num_of_advertisement_checkbox + 1

for turn in task_var:
    date = turn[1]
    name_of_selling = turn[2]
    selling_category1 = turn[3]
    selling_category2 = turn[4]
    payment_method = turn[5]
    dong = turn[6]
    ho = turn[7]
    side = turn[8]
    price_of_selling_raw = turn[9]
    price_of_selling = price_of_selling_raw.replace(",", "").replace("만원", "")
    monthly_price = turn[10]
    supply_size = turn[11]
    private_size = turn[12]
    size_of_py = turn[13]
    possible_date = turn[14]
    conneter = turn[15]
    connetion_number = turn[16]
    owner_name = turn[17]
    owner_number = turn[18]
    checkbox = turn[19]
    point_of_chassis = turn[20]
    chassis = turn[21]
    point_repair = turn[22]
    repair = turn[23]
    characteristic = turn[24]
    memo = turn[25]
    province_of_address = turn[26]
    city_of_address = turn[27]
    town_of_address = turn[28]
    bunji_of_address = turn[29]
    road_address = turn[30]
    ad.web_control()
    if np.array_equal(turn, task_var[0]):
        ad.web_login_gov()
    ad.issue_architecture_register(road_address, bunji_of_address, name_of_selling, city_of_address, selling_category1,
                                   selling_category2, dong, ho)
    owner_data = ad.get_owner_data()
    owner_name = owner_data[0]  # 소유자 이름
    private_size_raw = owner_data[2]  # 전용면적 사이즈
    private_size_index = private_size_raw.find('.') + 3
    private_size = private_size_raw[:private_size_index]
    print(private_size)
    orel = '본인'
    if np.array_equal(turn, task_var[0]):
        ar.serve_web_control()
    del_space_name_of_apt = str(name_of_selling).replace(" ", "")
    ar.select_option(selling_category1, selling_category2, payment_method, province_of_address, city_of_address,
                     town_of_address, del_space_name_of_apt, price_of_selling, monthly_price, dong, ho, owner_name,
                     private_size, orel)

    Db.update_cell(update_col, 18, owner_name)
    Db.update_cell(update_col, 13, private_size)
    Db.update_cell(update_col, 12, ar.suplly_space_m2)
    Db.update_cell(update_col, 14, ar.suplly_space_py)
    Db.update_cell(update_col, 20, 'TRUE')
    update_col += 1
    ar.resister_continue()

    ## 완료변수 입력

ad.driver.close()
ar.driver.close()

print('ver.0.2완료')


"""
link_send link_detail            홍보확인서이미지변환버튼
팝업 확인버튼
link_send link_detail           이미지 첨부하기

btn_public btn_public03             원래화면에서 매물전송 누르기


변수 불러오기
for     변수 지정
        건축물대장 찾아오기
        물건 등록하기
        기존 변수 업데이트
완료메세지



"""
