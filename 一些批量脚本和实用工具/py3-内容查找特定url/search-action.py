#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading
import time
import os
import re
import requests
from queue import Queue
import requests



# 存放内容
http_URL = []

#网站url
http_website  = []
#每个线程分配的url
urlSepList=[]
#分离文件名 给每个线程分一个
def read_file(file_path):
    # 判断文件路径是否存在，如果不存在直接退出，否则读取文件内容
    if not os.path.exists(file_path):
        print('Please confirm correct filepath !')
        sys.exit(0)
    else:
        with open(file_path, 'r') as source:
            for line in source:
                #print(line.rstrip('\r\n').rstrip('\n'))
                http_website.append(line.rstrip('\r\n').rstrip('\n'))

#分离文件名 给每个线程分一个
def separateName(threadCount):
    for i in range(0,len(http_website),int(len(http_website)/threadCount)):
        urlSepList.append(http_website[i:i+int(len(http_website)/threadCount)])

#多线程函数
def multithreading(threadCount):
    separateName(threadCount)#先分离
    for i in range(0,threadCount-1):
        t=threading.Thread(target=run_one_thread,args=(urlSepList[i],))
        t.start()

#每个线程的运作 参数为文件名称的列表
def run_one_thread(url_list):
    for url in url_list:
        website = url
        try:
            r = requests.get(url,timeout=5)
        except Exception as e:
            print ("error website:"+url)
            continue
        data = r.text
   	    # 利用正则查找所有连接
        link_list = re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')", data)
        ok_f=open("has_actionurl.txt","a+")
        for url in link_list:
            filename = os.path.basename(url)  # 取出文件名
            (shotname, extension) = os.path.splitext(filename)  # 取出文件后缀
            if extension == ".action":  # 指定后缀检测
                if 'http://' not in url:  # 检测是否有HTTP://
                    url = website + url
                    print(url)
                    ok_f.write(url+"\n")
                    http_URL.append(url)    # 读取到列表里或者写入文件中
                else:
                    print(url)
                    ok_f.write(url+"\n")
                    http_URL.append(url)
        ok_f.close()
if __name__ == '__main__':
    file_str="test.txt"
    read_file(file_str)
    multithreading(100)
    #print(urlSepList)