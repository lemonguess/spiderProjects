# -*-coding:utf-8-*-
from bs4 import BeautifulSoup
import requests
url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
response = requests.get(url)
print(type(response))
print(response.encoding)
page_text = requests.get(url=url,headers = headers)
page_text.encoding = 'UTF-8'
page_text = page_text.text
soup = BeautifulSoup(page_text,'lxml')
list_ = soup.select('.book-mulu > ul > li')
fp = open('./三国演义.text','w',encoding='utf-8')
for li in list_:
    title = li.a.string
    detail_url = 'https://www.shicimingju.com'+li.a['href']
    #对详情页发起请求，解析出章节内容
    detail_page = requests.get(url=detail_url,headers=headers)
    detail_page.encoding = 'utf-8'
    detail_pagetext = detail_page.text
    #解析出详情页中相关的章节内容
    detail_soup = BeautifulSoup(detail_pagetext,'lxml')
    div_tag=detail_soup.find('div',class_='chapter_content')
    #解析到章节的内容
    content = div_tag.text

    fp.write(title+':'+content+'\n')
    print(title,'爬取成功')


