# WeblogicScan
Weblogic一键批量漏洞检测工具，V1.0

	软件作者：Bywalks
	免责声明：Pia!(ｏ ‵-′)ノ”(ノ﹏<。)
	本工具仅用于安全测试，请勿用于非法用途，否则造成的一切后果自负~
	本版本为基于rabbitmask的WeblogicScan工具修改而成
	基于我的需求做了部分优化
        
	V 1.0使用方法：
	    需检测Links放入ScanUrl.txt
	    使用命令：python3 WeblogicScan.py
	    查看Weblogic.log即可查看所有Links的扫描结果
	
	V 1.0功能介绍：
	提供一键poc检测，收录几乎全部weblogic历史漏洞。
	详情如下：
	
        #控制台路径泄露
        Console  
        
        #SSRF：
        CVE-2014-4210      
        
        #JAVA反序列化
        CVE-2016-0638  
        CVE-2016-3510   
        CVE-2017-3248   
        CVE-2018-2628 
        CVE-2018-2893
        CVE-2019-2725
        CVE-2019-2729
        
        #任意文件上传
        CVE-2018-2894   
        
        #XMLDecoder反序列化
        CVE-2017-3506
        CVE-2017-10271 
        
        V 1.0 更新日志:
            批量扫描
            结果优化

Software using Demo:	
===
	__        __   _     _             _        ____
	\ \      / /__| |__ | | ___   __ _(_) ___  / ___|  ___ __ _ _ __
	 \ \ /\ / / _ \ '_ \| |/ _ \ / _` | |/ __| \___ \ / __/ _` | '_ \
	  \ V  V /  __/ |_) | | (_) | (_| | | (__   ___) | (_| (_| | | | |
	   \_/\_/ \___|_.__/|_|\___/ \__, |_|\___| |____/ \___\__,_|_| |_|
				     |___/
				     By Bywalks | V 1.0

	Welcome To WeblogicScan !!!
	Whoami：www.bywalks.com
	Usage: python3 WeblogicScan [IP] [PORT]
	[*]Console path is testing...
	[+]The target Weblogic console address is exposed!
	[+]The path is: http://127.0.0.1:7001/console/login/LoginForm.jsp
	[+]Please try weak password blasting!
	[*]CVE_2014_4210 is testing...
	[+]The target Weblogic UDDI module is exposed!
	[+]The path is: http://127.0.0.1:7001/uddiexplorer/
	[+]Please verify the SSRF vulnerability!
	[*]CVE_2016_0638 is testing...
	[-]Target weblogic not detected CVE-2016-0638
	[*]CVE_2016_3510 is testing...
	[-]Target weblogic not detected CVE-2016-3510
	[*]CVE_2017_3248 is testing...
	[-]Target weblogic not detected CVE-2017-3248
	[*]CVE_2017_3506 is testing...
	[-]Target weblogic not detected CVE-2017-3506
	[*]CVE_2017_10271 is testing...
	[-]Target weblogic not detected CVE-2017-10271
	[*]CVE_2018_2628 is testing...
	[-]Target weblogic not detected CVE-2018-2628
	[*]CVE_2018_2893 is testing...
	[-]Target weblogic not detected CVE-2018-2893
	[*]CVE_2018_2894 is testing...
	[-]Target weblogic not detected CVE-2018-2894
	[*]CVE_2019_2725 is testing...
	[+]The target weblogic has a JAVA deserialization vulnerability:CVE-2019-2725
	[+]Your current permission is:  bywalks\bywalks
	[*]CVE_2019_2729 is testing...
	[+]The target weblogic has a JAVA deserialization vulnerability:CVE-2019-2729
	[+]Your current permission is:  bywalks\bywalks
	[*]Happy End,the goal is 127.0.0.1:7001	

