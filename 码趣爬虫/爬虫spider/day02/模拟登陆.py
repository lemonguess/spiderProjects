import requests
"""
 cookie 简单的说就是维持登陆状态

"""
url = "http://ptlogin.4399.com/ptlogin/login.do?v=1"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
}
data = {
    "username":"15348438633",
    "password":"jingluo"
}
response = requests.post(url=url, headers=headers,data=data)
print(response.cookies)
print(requests.utils.dict_from_cookiejar(response.cookies))

# 4399群组广场 这一块其实没有登录
forums_url="http://my.4399.com/forums/"
resp = requests.get(url=forums_url,headers=headers,cookies = requests.utils.dict_from_cookiejar(response.cookies))
resp.encoding=resp.apparent_encoding
print(resp.text)