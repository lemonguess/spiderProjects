#coding=utf-8
import requests
import time
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
urls = {
    'https://downsc.chinaz.net/Files/DownLoad/flash2/201809/flash6481.rar',
    'https://downsc.chinaz.net/Files/DownLoad/flash2/202106/flash8714.rar',
    'https://downsc.chinaz.net/Files/DownLoad/flash2/202106/flash8716.rar'

}
start = time.time()
def get_content(url):
    print('正在爬取：',url)
    response = requests.get(url=url,headers = headers)
    if response.status_code == 200:
        return response.content
def parse_content(content):
    print('响应数据的长度为：',len(content))
i=0
for url in urls:

    content = get_content(url)
    parse_content(content)
    i += 1
end = time.time()
print(f'工作耗时： {end-start}s')