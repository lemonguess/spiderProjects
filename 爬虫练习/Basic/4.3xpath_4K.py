from lxml import etree
import requests
import re
import os
s = requests.Session()
#爬取页面源码数据
# if not os.path.exists('G:/壁纸/动漫'):
#     os.mkdir('G:/壁纸/动漫')
headers = {
    #'cookie':'__yjs_duid=1_ee05df81f9f194630ef6de21d49849081618771686108; Hm_lvt_14b14198b6e26157b7eba06b390ab763=1618771685; zkhanlastsearchtime=1623882123; Hm_lvt_526caf4e20c21f06a4e9209712d6a20e=1622620565,1623877186,1623880744,1623885582; PHPSESSID=p548rka519n7n3bp3tsnoet6e6; zkhanmlusername=%C0%F6%D4%C6%D0%C7%B3%BD; zkhanmluserid=4825910; zkhanmlgroupid=2; zkhanmlrnd=7KeK8Ne7DjE88WtdGg19; zkhanmlauth=8956eb69ed6eb39374d56aca2a7579ec; Hm_lpvt_526caf4e20c21f06a4e9209712d6a20e=1623885707',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}
# urls=["https://pic.netbian.com/4kdongman/",]
urls=[]
for i in range(2,100):
    url_ = f'https://pic.netbian.com/4kdongman/index_{i}.html'
    urls.append(url_)
print(urls)
for url in urls:
    try:
        page_text = requests.get(url=url,headers = headers)
    except Exceptions as e:
        print(e)
    page_text.encoding = 'gbk'
    page_text = page_text.text
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//*[@id="main"]/div[3]/ul/li')

    #print(img_detail)
    for li in li_list:
            #img_detail = 'https://pic.netbian.com'+li.xpath('./a/@href')[0]
            #print(img_detail)
            #id =''.join(re.findall('\d',img_detail))
            try:
                name = li.xpath('./a/b/text() | ./a/b/i/text()')[0]+'.jpg'
            except:
                print('正在下载... ...')
                            
            print(name)
            print(id)
            print(name,'正在下载... ...')

            down_url='https://pic.netbian.com/'+li.xpath('./a/b/img/@src')[0]
            img = s.get(url=down_url,headers = headers).content
            with open(f'G:/壁纸/动漫/{name}','wb') as fp:
                fp.write(img)
            print('下载成功！')
            # print(detail_page_text)
            # detail_tree = etree.HTML(detail_page_text)
            # img_url = 'https://pic.netbian.com'+ detail_tree.xpath('//iframe/@src')[0]
            # img_name = detail_tree.xpath('//*[@id="main"]/div[2]/div[1]/div[1]/h1')[0]+'.jpg'
            # #请求图片进行持久化存储
            # img_data = requests.get(url=img_url,headers=headers).content
            # img_path = 'G:/壁纸/动漫/'+img_name
            # with open('./01.html','w') as fp:
            #     fp.write(detail_page_text)
            #     # print(img_name,'下载成功！！')
