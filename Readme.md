# EmailFetch

## 项目简介
> 按照设置好的时间任务规则，去获取指定用户发送的指定邮件附件，并保存在指定位置
## 功能特性
1. > 定时任务
2. > 自动登录邮箱
3. > 获取并保存附件
## 环境依赖
- python 3.6.x
## 部署步骤
1. > 安装python环境，推荐使用miniconda，并建立虚拟环境:

`$ conda create -n emailFetch python=3.6`  
2. > 更改项目根目录(/emailAttFetch)下 ***emailFetch.bat*** 中相应的文件路径，主要有两点：

    - 虚拟环境 python.pyw 的文件路径
    - 项目文件timeTask的文件路径
3. > 更改 config.ini 相应的配置   
    - 仅更改server和path下对应的本地路径
4. 将emailFetch.bat放到windows的启动文件夹下，便于开机启动(<font color=green>  *C:\ProgramData\Microsoft\Windows\Start Menu\Programs\==StartUp==*</font>  )
---
---
---
## 目录结构描述
**emailAttFetch**
- <font color=blue>logFiles</font>  (日志文件夹)
    - <font color=blue>emailFetch.log</font>  (日志文件)
- <font color=blue>config.ini</font>  (配置文件)
- <font color=blue>initCfg.py</font>  (初始化配置文件)
- <font color=blue>emailAttDown.py</font>  (主功能代码文件)
- <font color=blue>loggingModule.py</font>  (日志格式化代码文件)
- <font color=blue>timeTask.pyw</font>  (定时任务代码文件)
- <font color=blue>requirements.txt</font>  (依赖包文件)
- <font color=blue>Readme.md</font>  (说明文档)
- <font color=blue>emailFetch.bat</font> (windows开机启动脚本)

> (dist文件内容详述)基于上次操作优化部分内容，我将所有的代码用pyinstaller打包为exe文件，需要三步操作即可。这次无需安装python环境，已经打包在程序中
1. 更改config.ini文件中的内容，包括email信息和文件存储路径(需提前建立)
2. 更改emailFetch_1.bat文件中的路径，路径为本文件中timeTask.exe打包程序在本机的文件路径，并将其放入windows启动文件路径下，方便开机启动，(启动路径: C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp)
3. 第一次启动可双击exe文件，程序已经运行在后台
注意事项:logFiles文件夹和config.ini文件需和timeTask.exe在同一路径下，为程序需要读取的配置文件