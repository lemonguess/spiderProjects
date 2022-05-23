#coding=utf-8
import requests
import time
#导入线程池对应的类
from multiprocessing.dummy import Pool

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
urls = {
    'https://downsc.chinaz.net/Files/DownLoad/flash2/201809/flash6481.rar',
    'https://downsc.chinaz.net/Files/DownLoad/flash2/202106/flash8714.rar',
    'https://downsc.chinaz.net/Files/DownLoad/flash2/202106/flash8716.rar'

}
def get_content(url):
    print('正在爬取：',url)
    response = requests.get(url=url,headers = headers)
    if response.status_code == 200:
        return response.content
def parse_content(content):
    print('响应数据的长度为：',len(content))
i=0
start = time.time()


#实例化一个线程池对象
pool = Pool(3)
#将列表中每一个列表元素传递给get_content处理
pool.map(get_content,urls)


end = time.time()
print(f'工作耗时： {end-start}s')


