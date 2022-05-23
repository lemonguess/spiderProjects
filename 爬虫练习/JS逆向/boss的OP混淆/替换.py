import execjs
import re
from multiprocessing.dummy import Pool
def Decode(code):
    with open('test1.js', 'r', encoding='utf-8') as fp:
        js_encrypt = fp.read()
        js_code = execjs.compile(js_encrypt,cwd='node_modules')
        sign = js_code.call('b', code)
        #print(sign,type(sign))
        return sign

    fp.close()
def getNew():
    global new_codes
    new_codes=''

    with open('source.js','r', encoding='utf-8') as fp2:
        new_codes = fp2.read()
    #fp2.close()
    code = re.findall("b\('(.*?)'\)",new_codes)
    return code
    # fp2.close()
def gg(code):
    #print(code[0])
    # print(code)
    with open('code.js', 'w+', encoding='utf-8') as fp3:
        for i in range(len(code)):
            #print(len(code))
            new_code = Decode(code[i])
            new_codes.replace(code[i], new_code)
        fp3.write(new_codes)

code = getNew()
gg(code)
# pool=Pool(10)
# pool.map(gg,code)
# pool.close()
# pool.join()
# #Decode('0x352')