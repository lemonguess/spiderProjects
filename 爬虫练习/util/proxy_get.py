import re

from requests_html import HTMLSession

if __name__ == '__main__':
    session = HTMLSession()
    page = session.get(url='https://www.kuaidaili.com/free/inha/1/')
    page.encoding = page.apparent_encoding
    page_text = page.text
    ip = re.findall(r'<td data-title="IP">\s*?(\d*?\.\d*?\.\d*?\.\d*?)</td>',page_text)
    port = re.findall(r'<td data-title="PORT">\s*?(\d*?)</td>')
    print(ip)
