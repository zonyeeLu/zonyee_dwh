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
from pyhive import hive

def main():
    # xml_file = open("D:\\temp\\test.xml",'w+',encoding="utf-8")
    res = requests.get('http://www.stat-nba.com/index.php#superstarList')
    res.encoding = 'utf-8'
    # xml_file.write(str(res.text.replace(u'\xa9', u'')))
    soup = BeautifulSoup(res.content.decode('utf-8', 'ignore'), 'html')
    res = soup.find_all('div')
    # print("得分榜==>总分榜")
    # for tmp in get_content(res, 'superstarList', '0pts0'):
    #     # print(tmp)
    # print("得分榜==>场均得分榜")
    # for tmp in get_content(res, 'superstarList', '0pts1'):
    #     # print(tmp)
    # print("得分榜==>单场总分榜")
    # for tmp in get_content(res, 'superstarList', '0pts2'):
    #     # print(tmp)

    # insert_data()

def get_content(result,main_tag,sub_tag):
    list = []
    for str in result:
        if str.get('id') == main_tag:
            res1 = str.find_all('div')
            for str1 in res1:
                if str1.get('id') == sub_tag:
                    res2 = str1.find_all('div')
                    for str2 in res2:
                        res3 = str2.find_all('div')
                        for str3 in res3:
                            dict = {}
                            dict[str3.select('a')[0].get_text()]=str3.select('p')[0].get_text()
                            list.append(dict)
    return list

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
#
#     return  conn
# main
if __name__ == '__main__':
    main()