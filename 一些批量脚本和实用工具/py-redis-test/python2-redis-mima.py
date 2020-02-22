#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author: 偷来的代码,原作者：r0cky
"""
import socket
import sys

passwds = ['redis','root','oracle','password','p@ssw0rd','abc123!','123456','admin','abc123']

def check(ip, port, timeout):
    try:
        socket.setdefaulttimeout(timeout)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #print u"[INFO] connecting " + ip + u":" + port
        s.connect((ip, int(port)))
        #print u"[INFO] connected "+ip+u":"+port+u" hacking..."
        s.send("INFO\r\n")
        result = s.recv(1024)
        if "redis_version" in result:
            return u"IP:{0}存在未授权访问".format(ip)
        elif "Authentication" in result:
            for passwd in passwds:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip, int(port)))
                s.send("AUTH %s\r\n" %(passwd))
                # print u"[HACKING] hacking to passwd --> "+passwd
                result = s.recv(1024)
                if 'OK' in result:
                    return u"IP:{0} 存在弱口令，密码：{1}".format(ip,passwd)
                else:pass
        else:pass
        s.close()
    except Exception, e:
        pass

if __name__ == '__main__':
    # default Port
    port="6379"
    with open('butian1.txt','r') as  f:
        ips = f.readlines()
        for i in ips:
            ip = i.strip("\n")
            result = check(ip,port,timeout=1)
            print(result)