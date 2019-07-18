#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ******************************************************************************
# 程序名称:     spider_nba_playoff_game_info.py
# 功能描述:     获取季后赛对阵
# 输入参数:     无
# 创建人名:     zonyee_lu
# 创建日期:     20190718
# ******************************************************************************
# ******************************************************************************

from bs4 import BeautifulSoup
import requests
# from pyhive import hive
import re
import time

def main():
    global playoff_game_info_file
    playoff_game_info_file = open("D:\\temp\\playoff_game_info_file.txt", 'w+', encoding="utf-8")
    res = requests.get('http://www.stat-nba.com/playoffchart/{0}.html'.format('2018'))
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.content.decode('utf-8', 'ignore'), 'html')
    print(soup)
    res = soup.find_all('div')

def get_content(result,game_type,data_type,data_time,season,season_type):
    data_list=[]
    for str in result:
        if str.get('id')==season_type+ game_type:
            res1 = str.find_all('div')
            for str1 in res1:
                if str1.get('id') == game_type + data_type + data_time:
                    res2 = str1.find_all('div')
                    for str2 in res2:
                        res3 = str2.find_all('div')
                        for str3 in res3:
                            list = []
                            player_name = str3.select('a')[0].get_text();
                            player_id = re.findall(r"\d+",str3.select('a')[0].get('href'))[0]
                            player_type = re.findall(r"[a-zA-Z]+",str3.select('a')[0].get('href'))[0]
                            player_data = str3.select('p')[0].get_text().replace('\n','')
                            list.append(player_id)
                            list.append(player_name)
                            list.append(player_type)
                            list.append(player_data)
                            list.append(game_type)
                            list.append(data_type)
                            list.append(data_time)
                            list.append(season)
                            list.append(season_type)
                            data_list.append(list)
    return data_list

def writ_flie(list):
    for line in list:
        print(line)
        playoff_game_info_file.write(str(line).replace('[','').replace(']','').replace('\'',''))
        playoff_game_info_file.write('\n')

def get_season(result):
    season_list = [];
    for str in result:
        res1 = str.find_all('a')
        for str1 in res1:
            if str1.get('class') and (str1.get('class')[0] == 'chooser' or str1.get('class')[0] == 'chooserin'):
                tmp = re.findall(r"\d+", str1.get('href'))[0]
                if tmp in season_list:
                    continue
                else:
                    season_list.append(re.findall(r"\d+", str1.get('href'))[0])
            else:
                continue
    return season_list

def test(result):
    data_list=[]
    for str in result:
        if str.get('id')=='seasonall':
            res1 = str.find_all('div')
            for str1 in res1:
                if str1.get('id') == 'allpts0':
                    res2 = str1.find_all('div')
                    for str2 in res2:
                        res3 = str2.find_all('div')
                        for str3 in res3:
                            list = []
                            player_name = str3.select('a')[0].get_text();
                            player_id = re.findall(r"\d+",str3.select('a')[0].get('href'))[0]
                            player_type = re.findall(r"[a-zA-Z]+",str3.select('a')[0].get('href'))[0]
                            player_data = str3.select('p')[0].get_text().replace('\n','')
                            list.append(player_id)
                            list.append(player_name)
                            list.append(player_type)
                            list.append(player_data)
                            data_list.append(list)
    print(data_list)


# def insert_data():
#     con = hive_connect()
#     cur = con.cursor()
#     cur.execute("select * from default.test")
#     for result in cur.fetchall():
#         print(result)
#     cur.close()
#     con.close()
# def hive_connect():
#     conn = hive.Connection(host='192.168.64.131',
#                              port=10000,
#                              username = None,
#                              database = 'default')

    # return  conn

# main
if __name__ == '__main__':
    main()