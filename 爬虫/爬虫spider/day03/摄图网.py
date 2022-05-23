import requests
from xpinyin import Pinyin

P = Pinyin()  # 实例化
"""
 xpinyin
 很多多音字 用xpinyin 满足不了
 https://699pic.com/tupian/4204557.html 瞎填  url 是数字了  4204557 
"""

word = "%E6%AC%A7%E6%B4%B2%E6%9D%AF"
# url = "https://699pic.com/tupian/{}.html".format(P.get_pinyin(word,''))
url = "https://699pic.com/search/getKwInfo?kw={}".format(word)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
}
response = requests.get(url=url, headers=headers).json()
print(response)
st_url = response["data"]["pinyin"]

url = "https://699pic.com/tupian/{}.html".format(st_url)
print(url)
