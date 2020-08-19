import requests


url = 'http://apis.data.go.kr/1611000/AptListService/getLegaldongAptList'
queryParams = {'serviceKey' : '3YUl0cFJp1ZmDCE5SOkvsskQu4fTCMlpwz4qdmYz4jjtMrrh9038gesJ8PI5NPPoT79pr0juhvpfjEtSnNbjIg%3D%3D', 'bjdCode' : '2638010100', 'pageNo' : '1', 'numOfRows' : '10' }

request = requests.get(url, params=queryParams)
requests.Response

print(requests.Response)