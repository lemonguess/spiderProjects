import requests


for page in range(0, 101, 50):
    url = "https://tieba.baidu.com/f?kw=%E5%8C%97%E6%96%97&ie=utf-8&pn={}".format(page)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    }
    response = requests.get(url=url, headers=headers)
    with open(f"html/bd_{page}.html", 'w',encoding="utf-8")as f:
        f.write(response.text)
