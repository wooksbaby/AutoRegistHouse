import requests

headers = {'Content-Type': 'application/json; charset=utf-8'}
url = 'http://apis.data.go.kr/1611000/AptListService/getLegaldongAptList'
key_raw = '3YUl0cFJp1ZmDCE5SOkvsskQu4fTCMlpwz4qdmYz4jjtMrrh9038gesJ8PI5NPPoT79pr0juhvpfjEtSnNbjIg%3D%3D'
key = requests.utils.unquote(key_raw)
bjd_dode = '4119010800'
queryParams = {'ServiceKey': key, 'bjdCode': bjd_dode, 'pageNo': '1', 'numOfRows': '46'}

response = requests.get(url, headers=headers, params=queryParams)
test = response.text
print(response.url)
print('test:' + test)
print('완료')
1111111