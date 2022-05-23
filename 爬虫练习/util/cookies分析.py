cookie= 'acw_tc=0bdd34ce16267922344934416e01d5a82a99cdb070462a0dcc745850849fad; ' \
        'Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1626792235; lastCity=100010000; ' \
        'Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1626792237; ' \
        '__c=1626792238; __g=-; ' \
        '__a=74158548.1626792238..1626792238.1.1.1.1; ' \
        '__zp_stoken__=e7b3cfFsfZHtXLhcPLm5jaFYSXQ1LWx1hbGxXaHwrKQwfCAAVAkopfw4lA2lNHU88PF01HX4GeUJxKEI2IndMRD5fXXNFNQNKVwALRWpJPxpRBXtWUgZgKDhMK3kPRFxBDH4lIHccBk90NgYW'
cookie = {i.split('=')[0]: i.split('=')[1] for i in cookie.split('; ')}
for i in cookie:
    print(i,'\n')

'''
acw_tc=0bdd34ce16267932176235844e01d57fbe41f6b495edf79000801f2f5b9f67; 
__zp_stoken__=e7b3cfFsfZHtXLlYCLzokaFYSXQ1nABZQZHhXaHwrKRgfczZzSUopfw4lRF10DT88PF01HX4GeWxxIF02PWgjRwppDXVUS31NBGF%2BVXxJPxpRBXtWIhZZHH9MK3kPRBdBDH4lIHccBk90NgYW
'''
