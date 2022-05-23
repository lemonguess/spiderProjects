#coding=utf-8
from selenium import webdriver
from time import sleep
from lxml import etree
#实例化一个浏览器对象（传入浏览器的驱动程序）
bro = webdriver.Chrome(executable_path='D:/SoftwareSpace/python/chromedriver.exe')
#让浏览器发起一个指定url对应请求
bro.get('https://www.jd.com/')
#标签定位
serch_input = bro.find_element_by_id('key')
#标签交互
serch_input.send_keys('巴萨')


#获取浏览器当前页面的页面源码数据
page_text = bro.page_source


#点击搜索按钮
btn = bro.find_element_by_css_selector('button')
btn.click()
#执行一组JS代码
bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
sleep(2)
# with open('./药监局.html','w',encoding='utf-8') as fp:
#     fp.write(page_text)

#解析
# tree = etree.HTML(page_text)
# li_list=tree.xpath('//*[@id="gzlist"]/li')

bro.get('https://www.bilibili.com/')
sleep(5)

#回退
bro.back()
sleep(2)
#前进
bro.forward()
sleep(2)

#关闭浏览器
sleep(2)
#bro.quit()

