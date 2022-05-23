import rsa
import binascii

def rsa_encrypt(rsa_n,rsa_e,data):
    #公钥
    key = rsa.PublicKey(rsa_n,rsa_e)
    res = rsa.encrypt(data.encode(),key)
    return binascii.b2a_hex(res)

public_n = '30819f300d06092a864886f70d010101050003818d0030818902818100b231a2588df3a48d614084d22124b409076cbc386dc1dd877ca01bffddedd41a519ac83537dacaf7b797c2a9e4200bce661dc433e856963f928b1e4022d3a875fbe68a796c049a6df721e16c035e58936f0476279bed93129cc39768788dd48761df8e45c8eb2a9fe0bcab4ee9226d524a28c9a60878878fbdcca8bb344fb6a10203010001'
public_e = '10001' #一般都是这个

#把16进制数据转整数
rsa_n = int(public_n,16)
rsa_e = int(public_e,16)
data = 'hello world'
print(rsa_encrypt(rsa_n,rsa_e,data))