from selenium import webdriver
from time import sleep

bro = webdriver.Chrome(executable_path='D:/SoftwareSpace/python/chromedriver.exe')

bro.get('https://qzone.qq.com/index.html')

bro.switch_to.frame('login_frame')

a_tag = bro.find_element_by_id("switcher_plogin")
a_tag.click()

userName_tag = bro.find_element_by_id('u')
password_tag = bro.find_element_by_id('p')

sleep(2)

userName_tag.send_keys('137790410')
password_tag.send_keys('lxc13355506+')

sleep(2)

btn = bro.find_element_by_id('login_button')
btn.click()
sleep(3)

