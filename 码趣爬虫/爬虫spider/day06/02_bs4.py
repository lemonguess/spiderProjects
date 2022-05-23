from bs4 import BeautifulSoup

html = open('xpath2.html', 'r', encoding='utf-8').read()
soup = BeautifulSoup(html, 'html.parser')
print(soup.select('#testid>h2'))
print(soup.select_one('#testid>h2'))

print(soup.select('#testid>ol>li'))
print(soup.select('#testid>ul>li'))
print(soup.select('#testid li'))
print(soup.select_one('#testid li'))  # 只获取一个

print(soup.select('#testid li[code="84"]'))
print(soup.select('div>div:nth-child(1)')) #选取第一个div