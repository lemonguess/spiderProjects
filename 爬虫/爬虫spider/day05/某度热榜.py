from requests_html import HTMLSession

session = HTMLSession()

url = "https://top.baidu.com/board?tab=novel"
response =session.get(url=url)
print(response.html.xpath('//div[@class="intro_1l0wp"]/text()'))
print(response.html.xpath('//div[@class="content_1YWBm"]/a/text()'))