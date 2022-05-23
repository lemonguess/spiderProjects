import re
from requests_html import HTMLSession

session = HTMLSession()
url = "https://www.douyu.com/g_LOL"
response = session.get(url=url)
# print(response.text)

title = re.findall('"od":"(.*?)",',response.text)
print(title)