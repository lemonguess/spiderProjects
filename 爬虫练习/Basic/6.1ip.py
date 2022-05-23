import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
proxy = {
    'http': '112.20.86.148:8080'
}
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
user_agent = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) " +
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36"
    )

response = requests.get("https://gkcx.eol.cn/school/search",headers=headers,proxies=proxy)
response.encoding='utf-8'
print(response.text)

print(response.status_code)
dic = {"ERRORCODE": "0", "RESULT": [{"port": "34507", "ip": "218.6.105.6"}, {"port": "44140", "ip": "114.221.174.204"},
                                    {"port": "44273", "ip": "59.60.209.243"},
                                    {"port": "31793", "ip": "125.117.142.179"},
                                    {"port": "20859", "ip": "180.107.4.240"},
                                    {"port": "37342", "ip": "183.146.156.215"},
                                    {"port": "41562", "ip": "220.188.88.235"}, {"port": "31974", "ip": "218.1.201.97"},
                                    {"port": "45001", "ip": "222.189.104.13"},
                                    {"port": "37867", "ip": "223.221.79.237"}]}
ip = f'{dic["RESULT"][1]["ip"]}:{dic["RESULT"][1]["port"]}'
chrome_options = Options()
chrome_options.add_argument('--proxy-server=http://222.191.168.168:43751')
print('--proxy-server=http://'+'112.20.86.148:8080')
chrome_options.add_argument(f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36')
school_bro = webdriver.Chrome(executable_path='D:/SoftwareSpace/python/chromedriver.exe',
                              chrome_options=chrome_options)
school_bro.get('https://gkcx.eol.cn/school/search')

