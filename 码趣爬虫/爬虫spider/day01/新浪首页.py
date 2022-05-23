import requests

url = "https://www.sina.com.cn/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
}
response = requests.get(url=url, headers=headers)
# print(response.text)
# print(response.encoding)
# print(response.apparent_encoding)
# response.encoding = "utf-8"
response.encoding = response.apparent_encoding  # 专业一点
# print(response.text)
print(response.content.decode())