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

headers = {'user-agent': 'ceshi/0.0.1'}

def islive(ur,port):
    url='http://' + str(ur)+':'+str(port)+'/uddiexplorer/'
    r = requests.get(url, headers=headers)
    return r.status_code

def run(url,port):
    if islive(url,port)==200:
        u='http://' + str(url)+':'+str(port)+'/uddiexplorer/'
        logging.info('[+]The target Weblogic UDDI module is exposed! The path is: {} Please verify the SSRF vulnerability!'.format(u))
        print('[+]The target Weblogic UDDI module is exposed!\n[+]The path is: {}\n[+]Please verify the SSRF vulnerability!'.format(u))
    else:
        print("[-]The target Weblogic UDDI module default path does not exist!")

if __name__=="__main__":
    url = sys.argv[1]
    port = int(sys.argv[2])
    run(url,port)
