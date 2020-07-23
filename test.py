import requests
import requests, bs4
import pandas as pd
from lxml import html
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote
from urllib import parse
from bs4 import BeautifulSoup


def getaptdata(roadcode):
    api_key = 'MqXYtq5mFWQq0D7XU%2Fahc88766ThoSj3PEpxXLJL71kJJAV%2F4NTJaoEYfyB064B1O5N6A3mX%2B%2BZzV4%2FKB83dIw%3D%3D'
    # http://coderstoolbox.net/string/#!encoding=url&action=decode&charset=utf_8
    # api_key_decode = unquote(api_key)

    # 출처: https://somjang.tistory.com/entry/SERVICE-KEY-IS-NOT-REGISTERED-ERROR [솜씨좋은장씨]
    # 별도 quote_plus() 메서드등 처리할 필요 없음. requests 객체가 알아서 해줌
    road_code = str(roadcode)
    url = 'http://apis.data.go.kr/1611000/AptListService/getRoadnameAptList?roadCode=' + road_code + '&ServiceKey=' + api_key
    # header_params = {"X-Naver-Client-Id":client_key, "X-Naver-Client-Secret":client_secret}
    # headers= header_params 는 header 변경시에만 필요하고, 그렇지 않으면, requests.get(원하는 URL) 만 해도 됨
    response = requests.get(url).text
    # headers = header_params)
    # 별도 json.loads() 라이브러리 메서드 사용하지 않아도, reqeusts 라이브러리에 있는 json() 메서드로 간단히 처리 가능함
    # print(response.json())
    # print(response.text)

    # HTTP 응답 코드는 status_code 에 저장됨
    data = response
    #print(data)
    soup = BeautifulSoup(data, "lxml")
    aptdata = []
    print(url)
    for item in soup.find_all("item"):
        unit = list((roadcode, item.find("kaptcode").get_text(), item.find("kaptname").get_text()))
        aptdata.append(unit)
    return aptdata


print(getaptdata(411903185015))
