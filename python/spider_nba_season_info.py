#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ******************************************************************************
# 程序名称:     spider_nba_records.py
# 功能描述:     获取nba历史记录
# 输入参数:     无
# 创建人名:     zonyee_lu
# 创建日期:     20190715
# ******************************************************************************
# ******************************************************************************

from bs4 import BeautifulSoup
import requests
# from pyhive import hive
import re
import time

def main():

    game_type=['all','1h','2h','1q','2q','3q','4q','5l','2l']
    data_type=['pts','trb','ast','blk','stl','tov','pf','ts','fg','fgper','threep','threepper','ft','ftper','g','kobe','per']
    data_time=['0','1','2']
    for season in range(2000,int(time.strftime("%Y"))):
        res = requests.get('http://www.stat-nba.com/season/{}.html'.format(season))
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.content.decode('utf-8', 'ignore'), 'html')
        res = soup.find_all('div')
        for game_tmp in game_type:
            for data_tmp in data_type:
                if game_tmp=='all':
                    for time_tmp in data_time:
                        if (data_tmp=='ts' or data_tmp=='threepper' or data_tmp=='ftper' or data_tmp=='g'or data_tmp=='fgper'or data_tmp=='per') and (time_tmp=='1' or time_tmp=='2'):
                            continue
                        else:
                            list = get_content(res,game_tmp,data_tmp,time_tmp,season)
                            print(list)
                else:
                    if data_tmp=='ts' or data_tmp=='threepper' or data_tmp=='ftper' or data_tmp=='g'or data_tmp=='fgper' or data_tmp=='per':
                        continue
                    list = get_content(res,game_tmp,data_tmp,'0',season)
                    print(list)

def get_content(result,game_type,data_type,data_time,season):
    data_list=[]
    for str in result:
        if str.get('id')=='season'+ game_type:
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
                            data_list.append(list)
    return data_list

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