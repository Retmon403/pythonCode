#https://fanyi.baidu.com/sug
#by:retmon
import requests
import json
import os

entry=input("输入要翻译的内容...")
post_url='https://fanyi.baidu.com/sug'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
data={'kw':entry}
response=requests.post(url=post_url,data=data,headers=headers)
json_str=json.dumps(response.json(),ensure_ascii=False)
js_dict=json.loads(json_str)
for i in js_dict['data']:
    for u in i.keys():
        print(i[u])
os.system('pause')