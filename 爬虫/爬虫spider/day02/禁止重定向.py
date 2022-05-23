import requests
"https://h5.pipix.com/item/6837720444338968835?app_id=1319&app=super&timestamp=1594730497&carrier_region=cn&region=cn&language=zh&utm_source=weixin"
url = "https://h5.pipix.com/s/JFfPN5J"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
}
response = requests.get(url=url, headers=headers,allow_redirects = False)
print(response.url)
