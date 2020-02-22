# !/usr/bin/env python
# -*- coding:utf-8 -*-

import gevent
from gevent import monkey

gevent.monkey.patch_all()
import requests as rq


def file_read(file_name="url.txt"):
    with open(file_name, "r") as f:
        return [i.replace("\n", "") for i in f.readlines()]


def check(url):
    '''
    if "http://" or "https://" not in url:
        url = "https://" + url
    '''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36 Edg/77.0.235.27',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Sec-Fetch-Site': 'none',
        'Accept-Charset': 'ZWNobyAiZWVTenh1OTJuSURBYiI7IA==',  # 输出 eeSzxu92nIDAb
        'Accept-Encoding': 'gzip,deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }
    try:
        #print(url)
        res = rq.get(url, headers=headers, timeout=3)
        if res.status_code == 200:
            res.text.find('eeSzxu92nIDAb')
            #print(res.text.find('eeSzxu92nIDAb'))
            if res.text.find('eeSzxu92nIDAb')>-1:
                print("[存在漏洞] " + url)
                f=open("ok.txt","a")
                f.write("[存在漏洞] " + url+"\n")
                f.close()
            else:
            	print("[不存在漏洞] " + url)
    except Exception as e:
        #raise e
        print("[超时] " + url)
if __name__ == '__main__':
    print("phpStudy 批量检测 (需要 gevent,requests 库)")
    print("使用之前，请将URL保存为 url.txt 放置此程序同目录下")
    input("任意按键开始执行..")
    tasks = [gevent.spawn(check, url) for url in file_read()]
    print("正在执行...请等候")
    gevent.joinall(tasks)
    wait = input("执行完毕 任意键退出...")