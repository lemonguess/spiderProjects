import se

url='https://movie.douban.com/top250?start=0&filter='

driver=selenium.webdriver.Chrome()
driver.get(url)
data = driver.page_source


file_path='D:/WorkSpace/pycharm/爬虫练习/douban.html'
with open(file_path,'w',encoding='utf-8') as f:
    f.write(data)

driver.close()