import requests

wd = "北斗"
url = f"https://www.baidu.com/sugrec?pre=1&p=3&ie=utf-8&json=1&prod=pc&from=pc_web&sugsid=34099,33971,31254,34133,34072,33607,34135,26350&wd={wd}&req=2&bs=%E9%B2%B8%E8%90%BD&csor=2&cb=jQuery11020026054767555675706_1624629889169&_=1624629889170"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
}
response = requests.get(url=url, headers=headers)
print(response.text)
