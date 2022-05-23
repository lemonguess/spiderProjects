import requests
import execjs
def getparam(query):
    pass
    with open('04.js','r',encoding='utf-8') as fp:
        js_encrypt = fp.read()
    js_code = execjs.compile(js_encrypt)
    sign = js_code.call('e', query)
    print(sign)
    return sign

def request():
    '''
    参数1：
        cookies=
        {'BAIDUID': 'A23815A1A4DAB5821A1D13E84420D843:FG',
         'Hm_lvt_64ecd82404c51e03dc91cb9e8c025574': '1626596208',
         'Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574': '1626596209',
         '__yjs_duid': '1_a2deae1dc55b432555b5124023cb5aaf1626596220542',}
     参数2：
        'sign': '471276.250845',
        'token': '49bad4afde2a7e6415e14c109dbed2a0',
    '''
    query = 'dog'
    sign = getparam(query)
    #print(sign)
    url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
    Cookie = 'BAIDUID=EEDE093BA2C53D9BA1A09DDF836FB031:FG=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1626597474; __yjs_duid=1_b8478e90bdad701cfdaa99465efcef501626597486102; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; __yjs_st=2_YzZmNDIyNTBlOTcyYTA2MWE3MjZjZGU3NjA4ZWI0NDE2MGQyOTNlYWM5ZTdiMWRkN2Y3NGEwY2JmZjBiZWFiM2Y2ODE3NjQ3ZWJlZmRkZGRhOWMzODBjYTg1NTJiYjJjNGRiMzQwZTFmZjVhOGU4ZWU3MDBmZjQxZjU0NTFhNTQxZTA3MTE2NzEzMzhmOGJhMTA1YjhmNmYxZmMwNjJkOGE1MzFmYjAyMjdlNzJhZjcwZmQwOGE4ZWZlMzdlNWE1MDlmMDI3Y2Y0ZWQ4NWYwM2MxYzUxMmE5OWUyNWY1MTUxMjUwNzlkMGYxZDRkZjY0YmFiYmJhNWI3ZWQ0MWQwN183XzYwNWQxM2I0; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1626602835; ab_sr=1.0.1_ZjE0YzBkYjQyNjVmYmJhNTFjMTY1ZDMyYTcxMzkxODc1ZTNhZTIxZTA1NjhkZjI5MDQxYjIwMDNiM2Q3OGIxYTZlYmRjYWFhNzkwMjZmMDA3OGU4NGNiMjE2ZWNkYzdmYjJiODc0Y2Y3MjA2NTczNWRiZDFkMmYyZjZiOGU1ZGJiODBmZjhkNjFhYjhjMzc3Y2FlYmQzNjI5NWM2NzcwYw=='
    cookies = {i.split('=')[0]: i.split('=')[1] for i in Cookie.split('; ')}
    #print(cookies)
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
    'Cookie':'BAIDUID=EEDE093BA2C53D9BA1A09DDF836FB031:FG=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1626597474; __yjs_duid=1_b8478e90bdad701cfdaa99465efcef501626597486102; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; __yjs_st=2_YzZmNDIyNTBlOTcyYTA2MWE3MjZjZGU3NjA4ZWI0NDE2MGQyOTNlYWM5ZTdiMWRkN2Y3NGEwY2JmZjBiZWFiM2Y2ODE3NjQ3ZWJlZmRkZGRhOWMzODBjYTg1NTJiYjJjNGRiMzQwZTFmZjVhOGU4ZWU3MDBmZjQxZjU0NTFhNTQxZTA3MTE2NzEzMzhmOGJhMTA1YjhmNmYxZmMwNjJkOGE1MzFmYjAyMjdlNzJhZjcwZmQwOGE4ZWZlMzdlNWE1MDlmMDI3Y2Y0ZWQ4NWYwM2MxYzUxMmE5OWUyNWY1MTUxMjUwNzlkMGYxZDRkZjY0YmFiYmJhNWI3ZWQ0MWQwN183XzYwNWQxM2I0; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1626602835; ab_sr=1.0.1_ZjE0YzBkYjQyNjVmYmJhNTFjMTY1ZDMyYTcxMzkxODc1ZTNhZTIxZTA1NjhkZjI5MDQxYjIwMDNiM2Q3OGIxYTZlYmRjYWFhNzkwMjZmMDA3OGU4NGNiMjE2ZWNkYzdmYjJiODc0Y2Y3MjA2NTczNWRiZDFkMmYyZjZiOGU1ZGJiODBmZjhkNjFhYjhjMzc3Y2FlYmQzNjI5NWM2NzcwYw=='
    }

    formdata = {
    'from': 'en',
    'to': 'zh',
    'query': query,
    'simple_means_flag': 3,
    'sign': sign,
    'token': '26cd065c5c99739ae449cf80fc2a247e',
    'domain': 'common'
    }
    response = requests.post(url=url,headers=headers,data = formdata)
    response.coding='utf-8'
    print(response.text)
#getparam('dog')
request()
