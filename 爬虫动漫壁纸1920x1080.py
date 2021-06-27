#http://www.netbian.com/dongman/index_2.htm
#by:retmon
import requests
import re
import os

def save_pic(i,data):
    f=open('pic\\'+str(i)+'.jpg','wb')
    f.write(data)
    f.close()

if os.path.exists('pic')==False:
    os.mkdir(os.getcwd()+'\\pic')
Phead='http://www.netbian.com'
page=1
cc=1
while True:
    if page==1:
        res=requests.get(Phead+'/dongman/')
    else:
        res=requests.get(Phead+'/dongman/index_'+str(page)+'.htm')
    res.encoding='gb2312'
    data=re.findall('/desk/\d+.htm',res.text)
    for i in data:
        res=requests.get(Phead+i)
        res.encoding='gb2312'
        ret=re.findall('.*src="(http.*?jpg)"\salt',res.text)
        print(ret[0])
        res=requests.get(ret[0])
        save_pic(cc,res.content)
        cc+=1
    page+=1