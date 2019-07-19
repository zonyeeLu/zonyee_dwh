#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ******************************************************************************
# 程序名称:     spider_nba_award_v2.py
# 功能描述:     荣誉排名数据
# 输入参数:     无
# 创建人名:     zonyee_lu
# 创建日期:     20190719
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
    get_top_data()

#获取总冠军数据
def get_champion_data():
    data_list = []
    champion_file = open("D:\\temp\\champion_file.txt", 'w+', encoding="utf-8")
    for year in range(2015, int(time.strftime("%Y")) + 1):
        res = requests.get('http://www.stat-nba.com/award/item15isnba1season{0}.html'.format(year))
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.content.decode('utf-8', 'ignore'), 'html')
        result = soup.find_all('tbody')
        for str in result:
            res = str.find_all('tr')
            for str1 in res:
                tmp_list = []
                tmp_list.append(year)
                res1 = str1.find_all('td')
                for str2 in res1:
                    tmp_list.append(str2.get_text())
                    if len(str2.select('a')) > 0:
                        tmp_list.append(re.findall(r"[a-z]+", str2.select('a')[0].get('href'))[0])
                        if re.findall(r"[a-z]+", str2.select('a')[0].get('href'))[0]=='player':
                            tmp_list.append(re.findall(r"[0-9]+", str2.select('a')[0].get('href'))[0])
                        if re.findall(r"[a-z]+", str2.select('a')[0].get('href'))[0] == 'team':
                            tmp_list.append(re.findall(r"[A-Z]+", str2.select('a')[0].get('href'))[0])
                tmp_list.append('15')
                data_list.append(tmp_list)
    writ_flie(data_list,champion_file)

#获取名人堂信息
def get_fame_player_data():
    data_list = []
    fame_player_file = open("D:\\temp\\fame_player_file.txt", 'w+', encoding="utf-8")
    for id in range(0,2):
        res = requests.get('http://www.stat-nba.com/award/item16isnba{0}.html'.format(id))
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.content.decode('utf-8', 'ignore'), 'html')
        result = soup.find_all('tbody')
        for str in result:
            res = str.find_all('tr')
            for str1 in res:
                tmp_list = []
                res1 = str1.find_all('td')
                for str2 in res1:
                    tmp_list.append(str2.get_text())
                    if len(str2.select('a')) > 0:
                        tmp_list.append(re.findall(r"[a-z]+", str2.select('a')[0].get('href'))[0])
                        if re.findall(r"[a-z]+", str2.select('a')[0].get('href'))[0] == 'player':
                            tmp_list.append(re.findall(r"[0-9]+", str2.select('a')[0].get('href'))[0])
                tmp_list.append('16')
                data_list.append(tmp_list)
    for temp in data_list:
        print(temp)
    writ_flie(data_list, fame_player_file)

#最佳阵容 最佳防守 最佳新秀
def get_best_team_data():
    data_list = []
    best_team_file = open("D:\\temp\\best_team_file.txt", 'w+', encoding="utf-8")
    type_list = [8,9,10]
    for year in range(2018, int(time.strftime("%Y")) + 1):
        for type_id in type_list:
            res = requests.get('http://www.stat-nba.com/award/item{0}isnba1season{1}.html'.format(type_id,year))
            res.encoding = 'utf-8'
            soup = BeautifulSoup(res.content.decode('utf-8', 'ignore'), 'html')
            result = soup.find_all('tbody')
            for str in result:
                res = str.find_all('tr')
                for str1 in res:
                    tmp_list = []
                    tmp_list.append(year)
                    res1 = str1.find_all('td')
                    for str2 in res1:
                        tmp_list.append(str2.get_text())
                        if len(str2.select('a')) > 0:
                            tmp_list.append(re.findall(r"[a-z]+", str2.select('a')[0].get('href'))[0])
                            if re.findall(r"[a-z]+", str2.select('a')[0].get('href'))[0] == 'player':
                                tmp_list.append(re.findall(r"[0-9]+", str2.select('a')[0].get('href'))[0])
                    tmp_list.append(type_id)
                    data_list.append(tmp_list)
    for temp in data_list:
        print(temp)
    writ_flie(data_list, best_team_file)

#全明星
def get_allstart_data():
    data_list = []
    allstart_file = open("D:\\temp\\allstart_file.txt", 'w+', encoding="utf-8")
    for year in range(2018, int(time.strftime("%Y")) + 1):
        res = requests.get('http://www.stat-nba.com/award/item12isnba1season{0}.html'.format(year))
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.content.decode('utf-8', 'ignore'), 'html')
        result = soup.find_all('tbody')
        for str in result:
            res = str.find_all('tr')
            for str1 in res:
                tmp_list = []
                tmp_list.append(year)
                res1 = str1.find_all('td')
                for str2 in res1:
                    if len(str2.get_text())>0:
                        tmp_list.append(str2.get_text())
                    if len(str2.select('a')) > 0:
                        tmp_list.append(re.findall(r"[a-z]+", str2.select('a')[0].get('href'))[0])
                        if re.findall(r"[a-z]+", str2.select('a')[0].get('href'))[0] == 'player':
                            tmp_list.append(re.findall(r"[0-9]+", str2.select('a')[0].get('href'))[0])
                tmp_list.append('12')
                if len(tmp_list)>2:
                    data_list.append(tmp_list)
    for temp in data_list:
        print(temp)
    writ_flie(data_list, allstart_file)

#月最佳 周最佳
def get_best_month_week_data():
    data_list = []
    allstart_file = open("D:\\temp\\allstart_file.txt", 'w+', encoding="utf-8")
    res = requests.get('http://www.stat-nba.com/award/item7.html')
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.content.decode('utf-8', 'ignore'), 'html')
    print(soup)

#选秀
def get_draft_data():
    data_list = []
    draf_file = open("D:\\temp\\draf_file.txt", 'w+', encoding="utf-8")
    for year in range(2018, int(time.strftime("%Y")) + 1):
        res = requests.get('http://www.stat-nba.com/award/item11isnba1season{}.html'.format(year))
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.content.decode('utf-8', 'ignore'), 'html')
        result = soup.find_all('tbody')
        for str in result:
            res = str.find_all('tr')
            for str1 in res:
                tmp_list = []
                tmp_list.append(year)
                res1 = str1.find_all('td')
                for str2 in res1:
                    tmp_list.append(str2.get_text())
                    if len(str2.select('a')) > 0:
                        tmp_list.append(re.findall(r"[a-z]+", str2.select('a')[0].get('href'))[0])
                        if re.findall(r"[a-z]+", str2.select('a')[0].get('href'))[0] == 'player':
                            tmp_list.append(re.findall(r"[0-9]+", str2.select('a')[0].get('href'))[0])
                        if re.findall(r"[a-z]+", str2.select('a')[0].get('href'))[0] == 'team':
                            tmp_list.append(re.findall(r"[A-Z]+", str2.select('a')[0].get('href'))[0])
                tmp_list.append('11')
                data_list.append(tmp_list)
    for temp in data_list:
        print(temp)
    writ_flie(data_list, draf_file)

def get_top_data():
    data_list = []
    top_file = open("D:\\temp\\top_file.txt", 'w+', encoding="utf-8")
    type_list=[0,1,2,3,4]
    type_name = ['得分王','篮板王','助攻王','盖帽王','抢断王']
    for type_id in type_list:
        res = requests.get('http://www.stat-nba.com/award/item14pr{0}.html'.format(type_id))
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.content.decode('utf-8', 'ignore'), 'html')
        result = soup.find_all('tbody')
        for str in result:
            res = str.find_all('tr')
            for str1 in res:
                tmp_list = []
                res1 = str1.find_all('td')
                for str2 in res1:
                    if len(str2.get_text()) > 0:
                        tmp_list.append(str2.get_text())
                    if len(str2.select('a')) > 0:
                        tmp_list.append(re.findall(r"[a-z]+", str2.select('a')[0].get('href'))[0])
                        if re.findall(r"[a-z]+", str2.select('a')[0].get('href'))[0] == 'player':
                            tmp_list.append(re.findall(r"[0-9]+", str2.select('a')[0].get('href'))[0])
                tmp_list.append('14')
                tmp_list.append(type_name[type_id])
                if len(tmp_list) > 2:
                    data_list.append(tmp_list)
    for temp in data_list:
        print(temp)
    writ_flie(data_list, top_file)

def get_content(result,type_id):
    data_list=[]
    for str in result:
        res = str.find_all('tr')
        for str1 in res:
            tmp_list = []
            res1 = str1.find_all('td')
            for str2 in res1:
                tmp_list.append(str2.get_text())
                if len(str2.select('a'))>0:
                    tmp_list.append(re.findall(r"[a-z]+",str2.select('a')[0].get('href'))[0])
                    tmp_list.append(re.findall(r"[0-9]+",str2.select('a')[0].get('href'))[0])
            tmp_list.append(type_id)
            data_list.append(tmp_list)
    return data_list

def writ_flie(list,file):
    for line in list:
        file.write(str(line).replace('[','').replace(']','').replace('\'',''))
        file.write('\n')

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