from lxml import etree
import requests
from pandas import Series,DataFrame
import re
#爬取页面源码数据
url = "https://nba.hupu.com/schedule/rockets"
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
page_text = requests.get(url=url,headers=headers).text
tree = etree.HTML(page_text)
#获取行数长度
i_max = page_text.count('<tr class="left">')
#print(i_max)
#获取列表表头
list_columns = tree.xpath('/html/body/div[3]/div[4]/table/tbody/tr[3]/td/text()')

list_index= []
#获取对阵列表
for i in range(1,i_max+1):
    team = tree.xpath(f'/html/body/div[3]/div[4]/table/tbody/tr[@class="left"][{i}]/td[@class="left"][1]/a/text()')
    num =  tree.xpath(f'/html/body/div[3]/div[4]/table/tbody/tr[@class="left"][{i}]/td[@class="left"][2]/text()')[0]
    jieguo = tree.xpath(f'/html/body/div[3]/div[4]/table/tbody/tr[@class="left"][{i}]/td[@class="left"][3]/text()')[0]
    time = tree.xpath(f'/html/body/div[3]/div[4]/table/tbody/tr[@class="left"][{i}]/td[@class="left"][4]/text()')[0]
    index_=[f'{team[0]}vs{team[1]}',re.sub(r'\n','',num),re.sub(r'\n','',jieguo),time]
    #print(team)
    list_index.append(index_)
#print(list_index)
data = DataFrame(data=list_index,columns=list_columns)
data.loc[~(data['比分'] == '-')]
print(data)
data.to_csv('./2020至2021赛季火箭队赛程.csv',columns=list_columns,encoding='utf-8')





