#coding=utf-8
import re
import requests
#导入线程池对应的类
from multiprocessing.dummy import Pool
from lxml import etree

session = requests.Session()
url = "https://www.pearvideo.com/category_1"
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
page_text = session.get(url=url,headers = headers).text

tree = etree.HTML(page_text)
li_list = tree.xpath('//ul[@id="listvideoListUl"]/li')
urls=[]#存储所有视频链接
for li in li_list:
    detail_url ='https://www.pearvideo.com/' + li.xpath('./div/a/@href')[0]
    name = li.xpath('./div/a/div[2]/test()')[0] + '.mp4'
    id = ''.join(re.findall('\d',detail_url))
    XHR_url = f'https://www.pearvideo.com/videoStatus.jsp?contId={id}'
    header={
    'Referer':f'https://www.pearvideo.com/video_{id}',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    }
    response_XHR = requests.get(url=XHR_url,headers = header).text
    vedio_url = re.findall('"srcUrl":"(.*?)"}}',response_XHR)[0]
    sub= re.findall('\d{8}/(.*?)-',vedio_url)[0]
    vedio_url = re.sub(sub,f'cont-{id}',vedio_url)
    dic={
        'name':name,
        'url':vedio_url
    }
    urls.append(dic)
    print(urls)

#使用线程池对视频数据进行请求(较为耗时的阻塞操作):
def get_video_date(dic):
    import time
    url=dic['url']
    print(dic["name"],"\n视频正在下载... ...")
    start=time.time()
    data=requests.get(url=url,headers=headers).content
    #持久化存储操作
    with open(dic['name'],'wb') as fp:
        fp.write(data)
        print(dic['name'],'视频下载成功！')
        end=time.time()
        time=end-start
        print(f'本次下载耗时：{time}s')
pool=Pool(4)
pool.map(get_video_date,urls)
pool.close()
pool.join()
