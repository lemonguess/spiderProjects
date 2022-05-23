from hashlib import md5

def md5_encryption(code):
    '''
    md5加密——方法返回对象
    :param code: str类型，要加密的字符串
    :return:str:返回加密后的字符串
    '''

    md = md5() #实例化——得到MD5加密对象
    md.update(code.encode())  #生成加密数据
    return md.hexdigest()   #获取加密数据

if __name__ == '__main__':
    sign = md5_encryption('123456')
    print(sign,len(sign))