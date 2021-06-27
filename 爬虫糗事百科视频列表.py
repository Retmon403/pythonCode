#https://www.qiushibaike.com/video/page/
#by:retmon
import requests
import re
import os

if os.path.exists('qiushi')==False:
    os.mkdir(os.getcwd()+'\\qiushi')

for page in range(13):
    ponse=requests.get('https://www.qiushibaike.com/video/page/'+str(page+1)+'/')
    url=re.findall('/article/\d+" r',ponse.text)
    mp4list=re.findall('.*src="(//.*?mp4)".*',ponse.text)
    add=1
    for u in mp4list:
            f=open('qiushi\\'+str(add)+'.mp4','wb')
            ponse=requests.get('https:'+u)
            f.write(ponse.content)
            f.close()
            print(str(add)+".下载视频...")
            add+=1