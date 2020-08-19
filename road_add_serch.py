import requests
import requests, bs4
import pandas as pd
from lxml import html
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote
from urllib import parse
from bs4 import BeautifulSoup


def getroadadd(keyword):
    api_key = 'devU01TX0FVVEgyMDIwMDcyMDA4NDQyMjEwOTk2Nzk='
    currentPage = 1
    countPerPage = 10

    # 출처: https://somjang.tistory.com/entry/SERVICE-KEY-IS-NOT-REGISTERED-ERROR [솜씨좋은장씨]
    # 별도 quote_plus() 메서드등 처리할 필요 없음. requests 객체가 알아서 해줌
    key_word = str(keyword)
    url = 'http://www.juso.go.kr/addrlink/addrLinkApi.do?currentPage=1&countPerPage=10&keyword=' + key_word + '&confmKey=' + api_key
    # header_params = {"X-Naver-Client-Id":client_key, "X-Naver-Client-Secret":client_secret}
    # headers= header_params 는 header 변경시에만 필요하고, 그렇지 않으면, requests.get(원하는 URL) 만 해도 됨
    response = requests.get(url).text
    # headers = header_params)
    # 별도 json.loads() 라이브러리 메서드 사용하지 않아도, reqeusts 라이브러리에 있는 json() 메서드로 간단히 처리 가능함
    # print(response.json())
    # print(response.text)

    # HTTP 응답 코드는 status_code 에 저장됨
    print('url is: ' + url)
    data = response
    #print('data is: ' + data)
    soup = BeautifulSoup(data, "xml")
    aptdata = []

    '''
    a = soup.find("roadAddr")
    b = soup.find("roadAddrPart2")
    c = soup.find("rnMgtSn")
    '''

    for juso in soup.find_all("juso"):
        unit = list((juso.find("bdNm"), juso.find("roadAddrPart1"), juso.find("rnMgtSn")))
        aptdata.append(unit)

    if aptdata.__len__() == 0:
        print('에러')
        aptdata = '찾을수 없는 주소입니다.'


    return aptdata


print(getroadadd('중동 덕유1단지아파트'))
