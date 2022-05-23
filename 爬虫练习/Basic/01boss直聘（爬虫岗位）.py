#coding=utf-8
from selenium import webdriver
from time import sleep
import pandas as pd
from lxml import etree

li_list=[]
job_list = []
place_list = []
salary_list = []
c_name_list = []
fuli_list = []
details_list = []
bro = webdriver.Chrome(executable_path='D:/SoftwareSpace/python/chromedriver.exe')
for i in range(1,5):
    url = f'https://www.zhipin.com/c101190100/?query=%E7%88%AC%E8%99%AB&page={i}&ka=page-{i}'
    bro.get(url)
    sleep(3)
    page_text=bro.page_source
    tree = etree.HTML(page_text)
    li_list=tree.xpath('//*[@id="main"]/div/div[3]/ul/li')
    for li in li_list:
        try:
            job = li.xpath('./div/div[1]/div[1]/div/div[1]/span[1]/a/test()')[0]
            place = li.xpath('./div/div[1]/div[1]/div/div[1]/span[2]/span/test()')[0]
            salary = li.xpath('./div/div[1]/div[1]/div/div[2]/span/test()')[0]
            c_name = li.xpath('./div/div[1]/div[2]/div/h3/a/test()')[0]
            fuli = li.xpath('./div/div[2]/div[2]/test()')[0]
            detail_url = 'https://www.zhipin.com'+ li.xpath('./div/div[1]/div[1]/div/div[1]/span[1]/a/@href')[0]
        except IndexError as e:
            print('li标签中有空值！')
        #获取详情页中的职位描述
        d_bro = webdriver.Chrome(executable_path='D:/SoftwareSpace/python/chromedriver.exe')
        bro.get(detail_url)
        page_text=bro.page_source
        d_tree = etree.HTML(page_text)
        detail = d_tree.xpath('//*[@id="main"]/div[2]/div/div[2]/div[2]/div[1]/div//test()')
        details=''.join(detail)
        d_bro.quit()

        job_list.append(job)
        place_list.append(place)
        salary_list.append(salary)
        c_name_list.append(c_name)
        fuli_list.append(fuli)
        details_list.append(details)
        print(job,place,salary,c_name,details,fuli)
# for li in li_list:
# result = etree.tostring(li,encoding='utf-8')
# li_text = result.decode('utf-8')
# with open('./li_text.html','w',encoding='utf-8') as fp:
#     fp.write(li_text)
# print(li_text)

# with open("zhiping.html", "r",encoding='utf-8') as f1:  # 打开文件
#     oli = f1.read()  # 读取文件
# litree = etree.HTML(oli)




#数据存储
job_pd = pd.DataFrame(job_list)
place_pd = pd.DataFrame(place_list)
salary_pd = pd.DataFrame(salary_list)
c_name_pd = pd.DataFrame(c_name_list)
fuli_pd = pd.DataFrame(fuli_list)
details_pd = pd.DataFrame(details_list)

boss_data = pd.concat([job_pd,place_pd,salary_pd,c_name_pd,details_pd,fuli_pd],axis=1)
boss_data.columns=['职位名称','工作地点','薪资待遇','公司名称','职位描述','公司福利']
boss_data.to_csv('./南京爬虫职位信息表.csv','w',sep=',',index=False,header=True,encoding='utf_8_sig')

# print(type(p))
# with open('./zhiping.html','w',encoding='utf-8') as fp:
#     fp.write(p)

# bro.quit()
