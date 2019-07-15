#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ******************************************************************************
# 程序名称:     spider_nba_player.py
# 功能描述:     获取nba球员以及教练信息
# 输入参数:     无
# 创建人名:     zonyee_lu
# 创建日期:     20190715
# ******************************************************************************
# ******************************************************************************

from bs4 import BeautifulSoup
import requests
import re

def main():
    # xml_file = open("D:\\temp\\test.xml",'w+',encoding="utf-8")
    for i in range(ord("A"), ord("Z") + 1):
        res = requests.get('http://www.stat-nba.com/playerList.php?il={0}&lil=0'.format(chr(i)))
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.content.decode('utf-8', 'ignore'), 'html')
        res = soup.find_all('div')
        list = get_content(res,'playerList')
        print(len(list))

def get_content(result,main_tag):
    list=[]
    for str in result:
        if (str.get('class') and str.get('class')[0]==main_tag):
                res1 = str.find_all('div')
                for str1 in res1:
                    sub_list=[]
                    player_name = str1.select('span')[0].get_text().replace('\n','')
                    player_info = str1.select('a')[0].get('href')
                    player_id = re.findall(r"\d+",player_info)[0]
                    player_type = re.findall(r"[a-zA-Z]+",player_info)[0]
                    sub_list.append(player_name)
                    sub_list.append(player_id)
                    sub_list.append(player_type)
                    list.append(sub_list)
    return list
# def test(result):
#     list=[]
#     for str in result:
#         if (str.get('class') and str.get('class')[0]=='playerList'):
#                 res1 = str.find_all('div')
#                 for str1 in res1:
#                     sub_list=[]
#                     player_name = str1.select('span')[0].get_text().replace('\n','')
#                     player_info = str1.select('a')[0].get('href')
#                     player_id = re.findall(r"\d+",player_info)[0]
#                     player_type = re.findall(r"[a-zA-Z]+",player_info)[0]
#                     sub_list.append(player_name)
#                     sub_list.append(player_id)
#                     sub_list.append(player_type)
#                     list.append(sub_list)
#     return list

# main
if __name__ == '__main__':
    main()