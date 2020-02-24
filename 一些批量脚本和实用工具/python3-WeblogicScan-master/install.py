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
import os

def run():
    os.system("pip install whl/certifi-2019.3.9-py2.py3-none-any.whl")
    os.system("pip install whl/chardet-3.0.4-py2.py3-none-any.whl")
    os.system("pip install whl/idna-2.8-py2.py3-none-any.whl")
    os.system("pip install whl/urllib3-1.25.2-py2.py3-none-any.whl")
    os.system("pip install whl/requests-2.22.0-py2.py3-none-any.whl")
    print ("install success!")

if __name__ == '__main__':
    run()
