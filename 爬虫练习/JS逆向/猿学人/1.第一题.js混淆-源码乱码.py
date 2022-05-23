import requests


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'}
url = 'http://match.yuanrenxue.com/api/match/1'
param = {'m': 'c36e2798cee570c1ac622042f09769ab丨1628849017'}
response = requests.get(url = url ,headers=headers,json=param)
print(response.text)