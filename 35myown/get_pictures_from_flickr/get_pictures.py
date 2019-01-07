#coding:utf-8

import flickrapi
import urllib.request
import os
import sys
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

API_KEY = "c5a46c9442dbac6784e974eb309a9f6f"
API_SECRET = "129746fe9b164d64"

#输入API的key和secret
flickr=flickrapi.FlickrAPI(API_KEY, API_SECRET, cache=True)
tag = "girl"
path = "./"+str(tag)+"/"
if not os.path.exists(path):
        os.makedirs(path)
try:
    #爬取tags为tag的照片,这里可以根据自己的需要设置其它的参数，还可以根据text
    photos=flickr.walk(tags=tag, extras='url_c')
    print(len(photos))
except Exception as e:
    print('Error')
count = 1
for photo in photos:
    #获得照片的url,设置大小为url_c(具体参数请参看FlickrAPI官方文档介绍)
    url=photo.get('url_c')
    if(str(url) == "None"):
        print("It's None!")
    else:
       #有效url进行爬取保存，文件名从1开始
        urllib.request.urlretrieve(url, path + str(count).zfill(7) + "." + os.path.basename(url).split(".")[1])
        count = count + 1
        print(url)
