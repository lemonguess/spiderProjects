#coding=utf-8
from selenium import webdriver
#实现无可视化界面
from selenium.webdriver.chrome.options import Options
#实现规避检测
from selenium.webdriver import ChromeOptions


#无头浏览器(无可视化界面)：
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')


#实现规避检测
option = ChromeOptions()
option.add_experimental_option('excludeSwitch',['enable-automation'])

bro = webdriver.Chrome(executable_path='D:/SoftwareSpace/python/chromedriver.exe',
                       chrome_options=chrome_options,
                       options=option)

bro.get('https://www.baidu.com')

p=bro.page_source
#p.encoding='utf-8'

print(p.encode('utf-8').decode)
