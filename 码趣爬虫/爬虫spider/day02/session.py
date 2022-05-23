import requests
"""
     requests.session() 会话保持 如果session登录 就会一直保持
        说白了就是比如你使用session成功的登录了某个网站，则在再次使用该session对象请求该网站的其他网页都会默认使用这个session 
        之前使用的cookie等参数 
    跨请求
        请求不同的网站就是跨请求携带同样的cookie等参数 (其实就是不同的网站  cookie和规则不同)
        在什么时候应用：
                1. 需要爬虫保持登录状态
                2. 爬虫需要携带一些特定的参数 比如购物网站的无登录状态下的推荐 主要是cookie
                    (没有登录的情况下给你推荐你喜欢的，他把商品的标签写进cookie了)
        HTTP API接口:
            只需要我们进行请求调用，传递特定的数据后api会返回数据，数据大多为 json/xml
        
        注意:
            先要进行session的实例化，实例化之后所有的请求都使用 实例化的变量进行get/post方法调用 如：session.post()
            requests.post() 这种方法将不会携带之前的cookie等参数 相当于重新来过

"""
url = "http://ptlogin.4399.com/ptlogin/login.do?v=1"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
}
data = {
    "username":"15348438633",
    "password":"jingluo"
}
session =requests.session()  # 会话维持

response = session.post(url=url, headers=headers,data=data)
print(response.cookies)
print(requests.utils.dict_from_cookiejar(response.cookies))

# 4399群组广场 这一块其实没有登录
# session带了cookie
forums_url="http://my.4399.com/forums/"
resp = session.get(url=forums_url,headers=headers)
resp.encoding=resp.apparent_encoding
print(resp.text)