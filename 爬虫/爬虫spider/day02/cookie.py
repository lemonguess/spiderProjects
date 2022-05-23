"""
    cookie 不安全 可以不知道你的账号密码 获取你的cookie 然后登录 不同的网站对cookie的操作是不一样的
    有些网站设置cookie只能在某个ip下使用 或者只能在某个浏览器下使用 构造cookie你要知道这个网站的后台开发构造cookie的规则

    cookie
        保持网站的登录状态，存储网站中某个特定的数据参数
        是有有效期的，超过有效期的cookie会被清除作废，所以在编写一个cookie爬虫代码的时候，并不是一次编写永久运行 每隔一段时间要更新cookie

    什么时候使用这种方法
        1. 当模拟登陆不好编写的时候(结构复杂，加密)
        2. 只有cookie 没有账号密码
        3.  网站根据cookie对用户进行推荐，专门爬取某人的个人推荐的时候
        ...
    在代码中利用cookie常用的两种方法
        1.  将cookie写入headers中
        2.  使用get方法中的cookies参数进行传递 注意：参数必须为字典类型
    注意：
        1.  自定义headers中的cookie 后面没有s(非cookies)
        2.  get方法中的cookies参数 cookies后面有s
        3.  cookie一定是键值对存在的
"""
import requests

url = "https://www.douban.com/"
# cookie = 'Cookie: ll="118267"; bid=a0LHpsvfLYA; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1624886722%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DHVMZCrT--7y-D4hwv5PfGW2n78m7_EuX7OLZVvO1Ne47n2G2pOVebf2-I7y6s-nm%26wd%3D%26eqid%3Dd974bcc10004ff710000000260d9cdbe%22%5D; _pk_ses.100001.8cb4=*; __utma=30149280.2105374173.1624886724.1624886724.1624886724.1; __utmc=30149280; __utmz=30149280.1624886724.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; dbcl2="239171598:m1j0J7wZhhY"; ck=5qBP; _pk_id.100001.8cb4=1a45953dd690767a.1624886722.1.1624886739.1624886722.; ap_v=0,6.0; __gads=ID=5718f1ee15c6cbb6-226406ba0aca00a4:T=1624886739:S=ALNI_MYxtZequbF83BhWbethviDsAkYC8g; push_noty_num=0; push_doumail_num=0; __utmv=30149280.23917; __utmb=30149280.3.10.1624886724'
#
# dic = {}
# for i in cookie.split("; "):
#     dic[i.split("=")[0]] = i.split("=")[1]
# print(dic)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    'Cookie': 'll="118267"; bid=a0LHpsvfLYA; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1624886722%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DHVMZCrT--7y-D4hwv5PfGW2n78m7_EuX7OLZVvO1Ne47n2G2pOVebf2-I7y6s-nm%26wd%3D%26eqid%3Dd974bcc10004ff710000000260d9cdbe%22%5D; _pk_ses.100001.8cb4=*; __utma=30149280.2105374173.1624886724.1624886724.1624886724.1; __utmc=30149280; __utmz=30149280.1624886724.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; dbcl2="239171598:m1j0J7wZhhY"; ck=5qBP; _pk_id.100001.8cb4=1a45953dd690767a.1624886722.1.1624886739.1624886722.; ap_v=0,6.0; __gads=ID=5718f1ee15c6cbb6-226406ba0aca00a4:T=1624886739:S=ALNI_MYxtZequbF83BhWbethviDsAkYC8g; push_noty_num=0; push_doumail_num=0; __utmv=30149280.23917; __utmb=30149280.3.10.1624886724'
}
response = requests.get(url=url, headers=headers)
print(response.text)
