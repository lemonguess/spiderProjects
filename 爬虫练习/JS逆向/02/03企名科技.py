import requests
import json
import execjs
start_url = 'https://www.qimingpian.cn/finosda/project/pinvestment'
def getResponse():
    form_data = {
            'tag':'',
            'unionid':''
    }
    response = requests.post(url='https://vipapi.qimingpian.com/Search/industryFieldVip',
                             headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'},
                             data = form_data
                )
    t = response.json()
    data = json.loads(response.text)['encrypt_data']
    return data
def main():

    data = getResponse()
    print(type(data),data)
    with open('03test_JS.js') as f:
        js_encrypt = f.read()
    ctx_encrypt = execjs.compile(js_encrypt)
    e=ctx_encrypt.call('decode',data)
    print(e)
    decrypt_data = ctx_encrypt.call('s',e)
    # json_data = json.loads(decrypt_data)
    # json_data.encoding='gbk'

    print(decrypt_data)


def test():
    with open('03test_JS.js') as f:
        js_encrypt = f.read()
    text = 'red yellow blue'
    ctx_encrypt = execjs.compile(js_encrypt)
    # decrypt_data = ctx_encrypt.call('decrypt',text)
    # decrypt_data.encoding = 'utf-8'
    # print(decrypt_data)

main()
#print(execjs.get().name)

