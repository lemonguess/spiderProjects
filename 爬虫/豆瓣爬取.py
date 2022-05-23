# -*- codeing = utf-8 -*-
from requests_html import HTMLSession
from lxml import etree
import re
#session = HTMLSession()
import requests
import pandas as pd

name = []
year = []
rate = []
director = []
scriptwriter = []
protagonist = []
genre = []
country = []
language = []
length = []
def getpage(page):
    for i in range(0,page+1):
        url = f'https://movie.douban.com/top250?start={page*25}&filter='
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'
        }
        response = requests.get(url=url,headers=headers).text
        tree = etree.HTML(response)
        li_list = tree.xpath('//*[@id="content"]/div/div[1]/ol/li')
        for li in li_list :
            name.append(li.xpath('./div/div[2]/div[1]/a/span[1]/text()')[0])
            year.append(li.xpath('./div/div[2]/div[2]/p[1]/text()[2]')[0])
            director.append(li.xpath('./div/div[2]/div[2]/p[1]/text()[1]')[0])
            country.append(li.xpath('./div/div[2]/div[2]/p[1]/text()[2]')[0])

if __name__ == '__main__':
    getpage(2)
    # 将list转化为dataframe
    name_pd = pd.DataFrame(name)
    year_pd = pd.DataFrame(year)
    rate_pd = pd.DataFrame(rate)
    director_pd = pd.DataFrame(director)
    scriptwriter_pd = pd.DataFrame(scriptwriter)
    protagonist_pd = pd.DataFrame(protagonist)
    genre_pd = pd.DataFrame(genre)
    country_pd = pd.DataFrame(country)
    language_pd = pd.DataFrame(language)
    length_pd = pd.DataFrame(length)
    





