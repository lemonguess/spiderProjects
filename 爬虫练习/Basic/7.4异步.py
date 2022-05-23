import asyncio
#加上async

async def get_html(url):
    print('正在下载',url)
    print('下载成功', url)
coroutine = get_html('www.baidu.com')
print(coroutine)