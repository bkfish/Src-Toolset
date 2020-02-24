#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
'''

Program：Weblogic Scan
Function：Weblogic All Version Vul Scan
 
Version：Python3
Time：2019/12/25
Author：bywalks
Blog：http://www.bywalks.com
Github：https://github.com/bywalks

'''
import logging
import sys
import requests 

VUL=['CVE-2018-2894']
headers = {'user-agent': 'ceshi/0.0.1'}

def islive(ur,port):
    url='http://' + str(ur)+':'+str(port)+'/ws_utc/resources/setting/options/general'
    r = requests.get(url, headers=headers)
    return r.status_code

def run(url,port,index):
    if islive(url,port)!=404:
        logging.info('[+]The target weblogic has a JAVA deserialization vulnerability:{}'.format(VUL[index]))
        print('[+]The target weblogic has a JAVA deserialization vulnerability:{}'.format(VUL[index]))
    else:
        print('[-]Target weblogic not detected {}'.format(VUL[index]))

if __name__=="__main__":
    url = sys.argv[1]
    port = int(sys.argv[2])
    run(url,port,0)
