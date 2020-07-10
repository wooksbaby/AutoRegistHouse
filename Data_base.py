from oauth2client.service_account import ServiceAccountCredentials
import gspread
import numpy as np

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'credentials.json', scope)

gc = gspread.authorize(credentials)
gc1 = gc.open('Restate stocks')
gc2 = gc1.worksheet('아파트정보')

heading_checkbox = gc2.find("광고현황")
heading_address_by_road = gc2.find("도로명")
heading_city_of_address = gc2.find("지번주소(시/도)")
heading_style_of_building = gc2.find("매물분류1")
heading_dong_apt = gc2.find("동")
heading_ho_apt = gc2.find("호")
heading_payment_method = gc2.find("거래종류")

check_box = gc2.col_values(heading_checkbox.col)
check_box2 = gc2.col_values(heading_payment_method.col)
start_row_num_of_advertisement_checkbox = check_box.index('FALSE')
# update_collape = start_row_num_of_advertisement_checkbox
end_col_num_of_advertisement = len(check_box2)
select_row = range(start_row_num_of_advertisement_checkbox + 1, end_col_num_of_advertisement + 1)

task_variable = np.array(gc2.row_values(start_row_num_of_advertisement_checkbox + 1))
for row in select_row[1::]:
    if row < end_col_num_of_advertisement+1:
        test = gc2.row_values(row)
        temp = np.array(test)
        task_variable = np.vstack((temp, task_variable))


def update_cell(update_of_col, cell_location_col,value):
    gc2.update_cell(update_of_col,cell_location_col,value)

"""
입력을 미리 해놓으면 입력값을 *알아서* 순차적으로 입력값 출력해옴
입력을 받을 정보는 주소 -->>

주소는 아파트명, 동, 호수로 받아옴

아파트명은 지역구로 나눠서 가져옴 아파트 단지데이터 필요함



 
 받아와서


"""
