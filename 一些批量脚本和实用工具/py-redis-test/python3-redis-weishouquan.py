#-*- coding:utf-8 -*-
import socket
from threading import Thread
from queue import Queue
from time import sleep,time
from urllib.parse import urlparse
def poc(url):
    url = url2ip(url)  # 将url转换成ip地址
    if url:
        port = int(url.split(':', -1)) if ':' in url else 6379 # redis默认端口是6379
        host = url.split(':')[0]
        payload = b'*1\r\n$4\r\ninfo\r\n' # 发送的数据
        s = socket.socket()      
        socket.setdefaulttimeout(3)  # 设置超时时间
        try:
            s.connect((host, port))
            s.send(payload)  # 发送info命令
            response = s.recv(1024).decode()
            s.close()
        
            if response and 'redis_version' in response:
                return True,'%s:%s'%(host,port)
        except (socket.error, socket.timeout):
            pass
    
    return False, None
def url2ip(url):
    """
    url转换成ip
    argument: url
    return: 形如www.a.com:80格式的字符串 若转换失败则返回None
    """
    try:
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'http://' + url
        ip = urlparse(url).netloc
        return ip
    except (ValueError, socket.gaierror):
        pass
    return None
 
def create_queue(file_name):
    """
    创建数据队列
    argument: file_name -> 输入文件名
    return: data,total 数据队列,数据总数
    """
    total = 0
    data = Queue()
    for line in open(file_name):
        url = line.strip()
        if url:
            # 跳过空白的行
            data.put(url)
            total += 1
    data.put(None)  # 结束标记
    return data,total
def start_jobs(data, num):
    """
    启动所有工作线程
    argument: data -> 数据队列 num -> 线程数
    """
    is_alive = [True]
    def job():
        """工作线程"""
        while is_alive[0]:
            try:
                url = data.get()
                if url == None:
                    # 遇到结束标记
                    break
                code, result = poc(url)  # 验证漏洞
                if code:
                    print(result)  # 存在漏洞
            except:
                is_alive[0] = False
        data.put(None)  # 结束标记
                
    jobs = [ Thread(target=job) for i in range(num) ]  # 创建多个线程
    for j in jobs:
        j.setDaemon(True)
        j.start()  # 启动线程
    for j in jobs:
        j.join()  # 等待线程退出
def main():
    import sys
    file_name = "butian.txt"  # 输入文件
    num = 1000  # 线程数
    data, total = create_queue(file_name)  # 创建数据队列
    print('total: %s' % total)
    begin = time()
    start_jobs(data, num)  # 启动工作线程
    end = time()
    print('spent %ss' % str(end-begin))
    
if __name__ == '__main__':
    main()