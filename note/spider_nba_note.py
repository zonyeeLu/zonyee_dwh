#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ******************************************************************************
# 程序名称:     spider_nba_note.py
# 功能描述:     将数据写入hdfs 笔记
# 输入参数:     无
# 创建人名:     zonyee_lu
# 创建日期:     20190715
# ******************************************************************************
# ******************************************************************************

# 在服务器中安装BeautifulSoup步骤
# 下载地址:http://www.crummy.com/software/BeautifulSoup/download/4.x/
# 推荐下载BeautifulSoup-4.2.1.tar.gz
# 解压缩:tar xvzf BeautifulSoup-4.2.1.tar.gz
# 进入beautifulsoup4-4.2.1文件
# 命令:python setup.py install
# 测试是否安装成功
# 输入python,
# >>from bs4 import BeautifulSoup
# 没有报告错误,安装成功、

# python3 安装 BeautifulSoup
# https://jingyan.baidu.com/article/ac6a9a5e31c87c2b643eac11.html

# 安装bs4遇到的问题:
# You are trying to run the Python 2 version of Beautiful Soup under Python 3
# 解决方案:
# 解决办法:直接将压缩文件中的bs4复制到python安装目录下的lib中,然后再利用python自带工具2to3.py将版本2下的.py 文件转化为版本3下的文件
# 具体:将bs4文件夹和2to3.py同时放到lib中,然后在cmd中定位到lib,运行:2to3 -w bs4就好了,最后需要将lib/bs4 覆盖/usr/local/Python3/lib/python3.6/site-packages之前的bs4
# 2to3 位置: /usr/local/Python3/bin

# 服务器中安装pip步骤
# https://pypi.python.org/pypi/pip
# 下载之后的包上传到服务器上
# 然后解压 tar -zxvf ***
# 解压之后会有个文件夹
# 进入到文件夹，执行命令python setup.py install
# 安装完之后执行 pip -V 如果能看到版本号，代表安装成功
# 如果报错-bash: pip: command not found
# 那么可以看一下是不是没有把python加入到环境变量中，如果没有添加一下，修改/etc/profile文件
# export PATH="$PATH:/usr/local/python/bin"  python 的路径一定要正确
# source /etc/profile
# 然后重新打开一个会话，执行pip -V  就可以看到了
# ok，安装成功了

# 安装pyhive 包
# pip install sasl
# pip install thrift
# pip install thrift-sasl
# pip install PyHive