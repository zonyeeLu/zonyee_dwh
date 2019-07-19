#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ******************************************************************************
# 程序名称:     spider_nba_award.py
# 功能描述:     荣誉信息
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
    global award_file
    award_file = open("D:\\temp\\award_file.txt", 'w+', encoding="utf-8")
    type_list=[0,1,2,3,4,5,6,17]
    for id in type_list:
        res = requests.get('http://www.stat-nba.com/award/item{}.html'.format(id))
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.content.decode('utf-8', 'ignore'), 'html')
        res = soup.find_all('tbody')
        writ_flie(get_content(res,id))

def get_content(result,type_id):
    data_list=[]
    for str in result:
        res = str.find_all('tr')
        # print(res)
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

def writ_flie(list):
    for line in list:
        award_file.write(str(line).replace('[','').replace(']','').replace('\'',''))
        award_file.write('\n')

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