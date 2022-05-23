#coding=utf-8
from selenium import webdriver
from time import sleep

#导入动作链对应的类
from selenium.webdriver import ActionChains
bro = webdriver.Chrome(executable_path='D:/SoftwareSpace/python/chromedriver.exe')

bro.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')

#如果定位的标签是存在于iframe标签之中，则必须通过如下操作再进行标签定位
bro.switch_to.frame('iframeResult')#切换浏览器标签定位的作用域
div=bro.find_element_by_id('draggable')

#动作链
action= ActionChains(bro)
#点击长按指定的标签
action.click_and_hold(div)

for i in range(5):
    #perform()立即执行动作链操作
    action.move_by_offset(17,0).perform()
    sleep(0.3)

#释放动作链
action.release()
print(div)

bro.quit()