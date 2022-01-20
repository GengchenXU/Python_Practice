'''
Description: 
Sample Intput: 
Output: 
Author: GengchenXu
CreateDate: 2021-08-08 20:06:25
LastEditTime: 2021-08-10 00:25:12
'''
import requests        #导入requests包
import json
def get_translate_date(word=None):
    url = 'https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    From_data={'i':'我嫩叠','from':'AUTO','to':'AUTO','smartresult':'dict','client':'fanyideskweb','salt':'16284371383907','sign':'f1c3b75ae1266bd1e61d198e6f972443','lts': '1628437138390','bv':'2e460ff55cc26efbf5d8b73602c006f8','doctype':'json','version':'2.1','keyfrom':'fanyi.web','action':'FY_BY_CLICKBUTTION'}
    #请求表单数据
    response = requests.post(url,data=From_data)
    #将Json格式字符串转字典
    content = json.loads(response.text)
    print(content)
    #打印翻译后的数据
    print(content['translateResult'][0][0]['src'])
if __name__=='__main__':
    get_translate_date('我爱中国')