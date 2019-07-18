#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ******************************************************************************
# 程序名称:     spider_nba_team_game.py
# 功能描述:     获取每个赛季球队战绩
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
    global team_game_data_file
    team_game_data_file = open("D:\\temp\\team_game_data_file.txt", 'w+', encoding="utf-8")
    for season in range(2000,int(time.strftime("%Y"))):
        res = requests.get('http://www.stat-nba.com/wper/{0}.html'.format(season))
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.content.decode('utf-8', 'ignore'), 'html')
        res = soup.find_all('table')
        writ_flie(get_content(res,season))

def get_content(result,season):
    data_list=[]
    for str in result:
        res1 = str.find_all('tr')
        for str1 in res1:
            res2 = str1.find_all('td')
            all_team_list=[]
            if len(res2)>0:
                team_list = []
                coach_list = []
                for str2 in res2:
                    tab_a = str2.find_all('a')
                    if len(tab_a)>1:
                        for tab_a_tmp in tab_a:
                            tmp_list=[]
                            if re.findall(r"[a-z]+",tab_a_tmp.get('href'))[0]=='coach':
                                tmp_list.append(re.findall(r"[0-9]+", tab_a_tmp.get('href'))[0])
                                tmp_list.append(re.findall(r"[a-zA-Z]+", tab_a_tmp.get('href'))[0])
                            tmp_list.append(tab_a_tmp.get_text())
                            tmp_list.append(str2.get_text())
                            coach_list.append(tmp_list)
                    if len(tab_a) == 1:
                        for tab_a_tmp in tab_a:
                            if re.findall(r"[a-z]+", tab_a_tmp.get('href'))[0] == 'team':
                                all_team_list.append(re.findall(r"[a-z]+",tab_a_tmp.get('href'))[0])
                                all_team_list.append(re.findall(r"[A-Z]+", tab_a_tmp.get('href'))[0])
                                all_team_list.append(str2.get_text())
                                team_list.append(re.findall(r"[a-z]+", tab_a_tmp.get('href'))[0])
                                team_list.append(re.findall(r"[A-Z]+", tab_a_tmp.get('href'))[0])
                                team_list.append(str2.get_text())
                            if re.findall(r"[a-z]+",tab_a_tmp.get('href'))[0]=='coach':
                                all_team_list.append(re.findall(r"[0-9]+", tab_a_tmp.get('href'))[0])
                                all_team_list.append(re.findall(r"[a-zA-Z]+", tab_a_tmp.get('href'))[0])
                                all_team_list.append(str2.get_text())
                                team_list.append(re.findall(r"[0-9]+", tab_a_tmp.get('href'))[0])
                                team_list.append(re.findall(r"[a-zA-Z]+", tab_a_tmp.get('href'))[0])
                                team_list.append(str2.get_text())
                    if len(tab_a)==0:
                        all_team_list.append(str2.get_text())
                        team_list.append(str2.get_text())

                if len(coach_list)>1:
                    for tmp_coach in coach_list:
                        tmp_team_list = []
                        tmp_team_list.append(team_list[0])
                        tmp_team_list.append(team_list[1])
                        tmp_team_list.append(team_list[2])
                        tmp_team_list.append(team_list[3])
                        tmp_team_list.append(team_list[4])
                        tmp_team_list.append(team_list[5])
                        tmp_team_list.append(team_list[6])
                        tmp_team_list.append(tmp_coach[0])
                        tmp_team_list.append(tmp_coach[1])
                        tmp_team_list.append(tmp_coach[2])
                        tmp_team_list.append(tmp_coach[3])
                        tmp_team_list.append(season)
                        data_list.append(tmp_team_list)
                else:
                    all_team_list.append('-')
                    data_list.append(all_team_list)
            all_team_list.append(season)
    return data_list

def writ_flie(list):
    for line in list:
        team_game_data_file.write(str(line).replace('[','').replace(']','').replace('\'',''))
        team_game_data_file.write('\n')

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