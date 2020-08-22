import requests
from bs4 import BeautifulSoup
from ast import literal_eval

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36 Edg/84.0.522.61'}

bjdcode = str(4119010800)

si_url = 'https://new.land.naver.com/api/regions/list?cortarNo='
si_response = requests.get(si_url, headers=headers)

si = si_response.json()

si_code = 'si_url에서 입력받기'

si_gun_url = 'https://new.land.naver.com/api/regions/list?cortarNo=' + si_code
si_gun_response = requests.get(si_gun_url, headers=headers)
si_gun = si_gun_response.json()

si_gun_code = 'si_url에서 입력받기'

gu_url = 'https://new.land.naver.com/api/regions/complexes?cortarNo=' + bjdcode + '&realEstateType=APT%3AABYG%3AJGC&order='
comp_response = requests.get(gu_url, headers=headers)

print(gu_url)

test = comp_response.json()

print(test['complexList'])