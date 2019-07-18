#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ******************************************************************************
# 程序名称:     spider_nba_game_sch.py
# 功能描述:     赛程信息
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
import datetime
from dateutil.relativedelta import relativedelta

def main():
    global game_sch_file
    game_sch_file = open("D:\\temp\\game_sch_file.txt", 'w+', encoding="utf-8")
    month=['01','02','03','04','05','06','07','08','09','10','11','12']
    for year in range(2018,int(time.strftime("%Y"))+1):
        for tmp_month in month:
            res = requests.get('http://www.stat-nba.com/gameList_simple-{0}.html'.format(str(year)+'-'+tmp_month))
            res.encoding = 'utf-8'
            soup = BeautifulSoup(res.content.decode('utf-8', 'ignore'), 'html')
            res = soup.find_all('tbody')
            writ_flie(get_content(res))

def get_content(result):
    data_list=[]
    for str in result:
        res = str.find_all('div')
        for str1 in res:
            if len(str1.select('font'))==1:
                # print(str1.select('font')[0].get_text())
                for tmp_game in str1.select('a'):
                    tmp_list = []
                    tmp_list.append(str1.select('font')[0].get_text())
                    tmp_list.append(re.findall(r"[a-z]+",tmp_game.get('href'))[0])
                    tmp_list.append(re.findall(r"[0-9]+",tmp_game.get('href'))[0])
                    tmp_list.append(re.findall(r"[\u4e00-\u9fa5]+",tmp_game.get_text().replace('76人','七十六人'))[0].replace('七十六人','76人'))
                    tmp_list.append(re.findall(r"[0-9]+",tmp_game.get_text().replace('76人','七十六人'))[0].replace('七十六人','76人'))
                    tmp_list.append(re.findall(r"[\u4e00-\u9fa5]+", tmp_game.get_text().replace('76人','七十六人'))[1].replace('七十六人','76人'))
                    tmp_list.append(re.findall(r"[0-9]+", tmp_game.get_text().replace('76人','七十六人'))[1].replace('七十六人','76人'))
                    data_list.append(tmp_list)
            if len(str1.select('font'))>1:
                tmp_list = []
                tmp_list.append(str1.select('font')[0].get_text())
                tmp_list.append('no_game')
                tmp_list.append('0')
                tmp_list.append('null')
                tmp_list.append('0')
                tmp_list.append('null')
                tmp_list.append('0')
                data_list.append(tmp_list)
    return data_list

def writ_flie(list):
    for line in list:
        game_sch_file.write(str(line).replace('[','').replace(']','').replace('\'',''))
        game_sch_file.write('\n')

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