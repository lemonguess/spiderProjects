from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


#配置键值对信息
caps = {
  "platformName": "Android",
  "platformVersion": "5",
  "deviceName": "127.0.0.1:62001",
  "appPackage": "com.netease.cloudmusic",
  "appActivity": ".activity.LoginActivity"
  }
# 链接Appium服务器,打开应用，返回驱动对象driver，接下来就和selenium的操作几乎一样
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)

#显示等待
'''
登录点击ID：com.netease.cloudmusic:id/f8
    手机号ID：com.netease.cloudmusic:id/a69
    密码ID：com.netease.cloudmusic:id/f7
    登录ID：com.netease.cloudmusic:id/f8
'''
wait=WebDriverWait(driver,20)
wait.until(EC.element_to_be_clickable((By.ID,'com.netease.cloudmusic:id/f8'))).click()

#输入账号密码
user_name = wait.until(EC.presence_of_element_located((By.ID,'com.netease.cloudmusic:id/a69')))
user_name.send_keys('18203220212')
password = wait.until(EC.presence_of_element_located((By.ID,'com.netease.cloudmusic:id/f7')))
password.send_keys('lxc13355506')
wait.until(EC.element_to_be_clickable((By.ID,'com.netease.cloudmusic:id/f8'))).click()

sleep(20)





