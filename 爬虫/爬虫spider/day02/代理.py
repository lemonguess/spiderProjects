"""
代理作用让我们爬虫不被人抓 三种代理
1 透明代理  直接访问网站 网站能看到你的ip
代理服务器将客户端的信息转发至目标访问对象，并没有完全隐藏客户端真实的身份，即服务器知道客户端使用了代理IP，并且完全知道客户端的真实ip
2 普通匿名代理
    代理服务器用自己的ip代理了客户端的真实IP 但是告诉了目标访问对象这是代理访问
3 高匿代理
  代理服务器良好的伪装了客户端，不但用一个随机的IP代理了客户端的IP 也隐藏了代理信息，服务器不会察觉到客户端是通过代理实现访问的
  就像一个真正的客户正在浏览网页，而客户的IP却被隐藏了.这样客户端就不会认为用户使用了代理，另外还可以保证用户的隐私

  你要别人电脑去访问网站

"""
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
}

proxie = {
    "http":"114.98.160.51:9999"
}
response = requests.get(url="http://httpbin.org/get", headers=headers,proxies=proxie)
print(response.text)
