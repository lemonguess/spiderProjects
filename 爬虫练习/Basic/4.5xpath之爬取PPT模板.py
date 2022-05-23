from lxml import etree
import requests
import os
import zipfile



headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
url_list = ['https://sc.chinaz.com/ppt/free.html']
i =2
#分页20
while i<21:
    url = f'https://sc.chinaz.com/ppt/free_{i}.html'
    url_list.append(url)
    i += 1
#创建下载文件文件夹
if not os.path.exists('./PPT'):
    os.mkdir('./PPT')
#遍历分页链接
detail_url_list = []
for url in url_list:
    page_text = requests.get(url=url,headers=headers).text
    tree = etree.HTML(page_text)
    detail_url = tree.xpath('//div[@class="container clearfix"]//div[@class="bot-div"]/a/@href')
    for i in detail_url:
        detail_url_list.append(i)
#遍历详情页链接
for detail_url in detail_url_list:
    detail_url = 'https://sc.chinaz.com/' + detail_url
    detail_page_text = requests.get(url=detail_url, headers=headers)
    detail_page_text.encoding = 'utf-8'
    detail_page_text = detail_page_text.text
    d_tree = etree.HTML(detail_page_text)
    download_url = d_tree.xpath('//div[@class = "download-url"]/a/@href')[0]
    download_name = d_tree.xpath('//div[@class = "title-box clearfix"]/h1/test()')[0]+'.zip'
#对已解析到的PPT下载链接及PPT名称进行下载和存储
    PPT_data = requests.get(url=download_url, headers=headers).content
    PPT_path = 'PPT/' + download_name
    with open(PPT_path,'wb') as fp:
        fp.write(PPT_data)
        print(download_name,'下载成功！！')

#文件的解压、修改和删除
# download_name = '略略略.zip'
#print('正在解压文件“download_name”，并删除多余文件...')
s = zipfile.ZipFile('./PPT/s.zip','r')
# z=zipfile.ZipFile('./PPT/z.zip')
#print(s.namelist())
# z.extract('m.ppt','./PPT')

print('保存成功！！')
