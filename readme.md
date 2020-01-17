应急工具集
```
│  readme.md
│  
├─Webshell查杀
│  │  D盾.7z
│  │  
│  └─Sangfor_Webshell查杀工具
│          wscan.rar
│          
├─专杀工具
│  ├─Parite专杀
│  │      antiparite-en.bat
│  │      avast.bat
│  │      ClnPinfi.bat
│  │      
│  ├─Ramnit专杀
│  │      FxRamnit.exe
│  │      
│  ├─Sality专杀
│  │      SalityKiller.exe
│  │      
│  ├─Spybot专杀
│  │      FixSpybot.exe
│  │      FxSpANDM.exe
│  │      
│  ├─Virut专杀
│  │      virut.exe
│  │      
│  ├─Zbot或Zeus专杀
│  │      zbotkiller.exe
│  │      
│  └─飞客蠕虫专杀
│          kidokiller.exe
│          TMCleanTool.rar
│          
├─信息收集工具
│  │  browsinghistoryview.zip
│  │  Fastir_Collector-master.zip
│  │  
│  └─browsinghistoryview
│          BrowsingHistoryView.cfg
│          BrowsingHistoryView.chm
│          BrowsingHistoryView.exe
│          readme.txt
│          
├─启动项分析工具
│      Autoruns.zip
│      
├─文档说明
│      Sality病毒分析与查杀.doc
│      Windows环境黑客入侵应急与排查.doc
│      应急工具集使用说明.doc
│      飞客蠕虫分析与查杀.doc
│      
├─流量分析工具
│  │  TCPView.zip
│  │  
│  ├─Wireshark32
│  │      Wireshark-win32-2.0.1.exe
│  │      
│  ├─Wireshark64
│  │      Wireshark_win64_V1.12.4_setup.1427187922.exe
│  │      
│  ├─Wireshark兼容XP
│  │      Wireshark-win32-1.10.9.exe
│  │      
│  ├─科来网络分析32
│  │      csnas_tech8.zip
│  │      
│  └─科来网络分析64
├─练手病毒样本
│  │  下载病毒样本前说明（重要）.txt
│  │  
│  ├─gbot
│  │      gbot.rar
│  │      
│  ├─lpk
│  │      lpk.zip
│  │      
│  ├─murofet
│  │      murofet.zip
│  │      
│  ├─ramnit
│  │      ramnit.rar
│  │      
│  ├─sality
│  │      sality.rar
│  │      
│  ├─sdbot
│  │      sdbot.rar
│  │      
│  ├─virut
│  │      virut.zip
│  │      
│  └─zeus
│          zeus.rar
│          
├─辅助工具
│  │  Everything-1.4.1.877.x86.en-US-Setup.exe
│  │  Everything_1.4.1.877_x64-Setup.exe
│  │  Hash.exe
│  │  ntfsdir.7z
│  │  regshot2.0.1.66.1403584153.zip
│  │  Strings.zip
│  │  Unlocker1.9.2.exe
│  │  winhex_19.1.0.0.zip
│  │  
│  └─Strings
│          Eula.txt
│          strings.exe
│          strings64.exe
│          
└─进程分析工具
        PCHunter_free.zip
        pd_latest.zip
        ProcessExplorer.zip
        ProcessHacker.zip
        ProcessMonitor.zip
        PSTools.zip
        Sysmon.zip
        XueTr.zip
```
应急工具集使用说明

### 1 进程分析工具
#### 1.1 ProcessHacker
功能：ProcessHacker是一款不错的进程分析工具，可查看所有进程信息，包括进程加载的dll、进程打开的文件、进程读写的注册表……，也可以将特定进程的内存空间Dump到本地，此外还可以查看网络连接。
工具截图如下：

注：查看具体进程的详细信息，双击Processes列表中的进程名字即可。
#### 1.2 ProcessExplorer
功能：ProcessExplorer是一款不错的进程分析工具，微软官方推荐工具，稳定性和兼容性相对不错。可查看所有进程的信息，包括其加载的dll、创建的线程、网络连接……，同样可以Dump出进程的内存空间到本地。


#### 1.3 ProcessMonitor
功能：ProcessMonitor是一款实时刷新的进程信息监控工具，微软官方推荐工具，稳定性和兼容性也是相对出色。展示的信息很全面，且每一个打开的句柄、注册表、网络连接……都与具体的进程关联起来。


#### 1.4 XueTr
功能：XueTr（官网www.xuetr.com）是一个Windows系统信息查看软件，可协助排查木马、后门等病毒，功能包含：
- 1.进程、线程、进程模块、进程窗口、进程内存、定时器、热键信息查看，杀进程、杀线程、卸载模块等功能
- 2.内核驱动模块查看，支持内核驱动模块的内存拷贝
- 3.SSDT、Shadow SSDT、FSD、Keyboard、TCPIP、Classpnp、Atapi、Acpi、SCSI、Mouse、IDT、GDT信息查看，并能检测和恢复ssdt hook和inline hook
- 4.CreateProcess、CreateThread、LoadImage、CmpCallback、BugCheckCallback、Shutdown、Lego等Notify Routine信息查看，并支持对这些Notify Routine的删除
- 5.端口信息查看
- 6.查看消息钩子
- 7.内核模块的iat、eat、inline hook、patches检测和恢复
- 8.磁盘、卷、键盘、网络层等过滤驱动检测，并支持删除
- 9.注册表编辑
- 10.进程iat、eat、inline hook、patches检测和恢复
- 11.文件系统查看，支持基本的文件操作
- 12.查看（编辑）IE插件、SPI、启动项、服务、Host文件、映像劫持、文件关联、系统防火墙规则、IME
- 13.ObjectType Hook检测和恢复
- 14.DPC定时器检测和删除
- 15.MBR Rootkit检测和修复
- 16.内核对象劫持检测
- 17.其它一些手工杀毒时需要用到的功能，如修复LSP、修复安全模式等

#### 1.5 PCHunter
功能：XueTr的增强版，功能和XueTr差不多，可参考上图。推荐更多使用PCHunter，减少出故障的概率。

#### 1.6 ProcessDump
功能：可对指定的进程，将其进程空间内的所有模块单独Dump出来，甚至可Dump出隐藏的模块（即进程加载的dll，这里通常是被注入）。

注：这是个命令行工具。

#### 1.7 PsTools
功能：PsTools是命令行工具集，微软官方推荐，功能多而全，其涵盖的子功能（命令）如下：


### 2 流量分析工具
#### 2.1 Wireshark
功能：Wireshark是一款常用的网络抓包工具，同时也可以用于流量分析。


#### 2.2 科来网络分析
功能：科来公司的一款流量分析工具，对比Wireshark要相对易用些（特别是流量分析入门人员），此外，该工具会自动将流量进行归类和统计。在某种意味上，还是比较方便的。



#### 2.3 TCPView
功能：查看系统的网络连接详情，每一条连接对应的进程、协议、进程、源目地址、源目端口、连接状态……总之，可展示当前活跃连接的所有详细信息。



### 3 启动项分析工具
#### 3.1 AutoRuns
功能：一款不错的启动项分析工具，微软官方推荐。只要涉及到启动项相关的信息，事无巨细，通通都可以查询得到，非常方便找到病毒的启动项。



### 4 信息收集工具
#### 4.1 FastIR
功能：收集操作系统的关键日志、关键信息，方便后续取证和排查分析。

#### 4.2 BrowsingHistoryView
功能：收集浏览器的历史记录，方便追溯域名、URL的访问来源是否源自于用户行为。


### 5 辅助工具
#### 5.1 Hash
功能：文件hash计算工具，可计算文件MD5、SHA1、CRC值，可用于辅助判断文件是否被篡改，或者使用哈希值到威胁情报网站查看是否为恶意文件。


#### 5.2 ntfsdir
功能：病毒也有可能是以创建服务启动项的方式保持长久运行，点击Autoruns的Services功能，如下图，检查是否有异常的服务启动项。

#### 5.3 Unlocker
功能：可对难以删除的文件进行强制删除（包括锁定的文件），需安装，安装后右键菜单”Unlocker“即可弹出如下界面：



### 6 Webshell查杀工具
#### 6.1 wscan
功能：深信服自研的一款Webshell查杀工具。


#### 6.2 D盾
功能：D盾是迪元素科技的一款Webshell查杀工具。



### 7 专杀工具
#### 7.1 飞客蠕虫专杀
功能：专门针对飞客蠕虫病毒进行查杀的工具。
飞客蠕虫专杀工具有kidokiller（卡巴斯基出品）、TMCleanTool（趋势科技出品）。
Kidokiller运行截图如下，红色方框的所有0值表明没有中飞客蠕虫，如果有非0值，即说明中了飞客蠕虫。
	
TMCleanTool的运行截图如下，有威胁项即表明中了飞客蠕虫。


#### 7.2 Ramnit专杀
功能：专门针对Ramnit类家族病毒进行查杀的工具
FxRamnit是赛门铁克出品的Ramnit专杀工具，其运行界面如下，点击”Start“按钮即可：

注：由于Ramnit是全盘感染性病毒，故此专杀工具运行时间比较长，需耐心等待（FxRamnit常常给人一种”假死“的感觉）。