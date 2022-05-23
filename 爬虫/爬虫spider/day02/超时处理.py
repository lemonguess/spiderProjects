import requests

url = "https://www.google.com/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
}
#设置了timeout之后，一旦超时，会发生报错，然后任务也就结束了。但是会保证每个任务的时间都是被限制了的。
response = requests.get(url=url, headers=headers,timeout=4)
print(response.text)