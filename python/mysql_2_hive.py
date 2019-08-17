#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ******************************************************************************
# 程序名称:     mysql_2_hive.py
# 功能描述:     抽取mysql数据到hive(无需加密)
# 输入参数:     无
# 创建人名:     zonyee_lu
# 创建日期:     20190813
# ******************************************************************************
# ******************************************************************************

# from bs4 import BeautifulSoup
# import requests
# import re
import pymysql
import os

def main():
    cols, create_str = get_table_info('component','localhost','root','kobe24','mysql',3306,'tmp')
    print(cols)
    print(create_str)

def get_mysql_conn(mysql_host,mysql_user,mysql_pw,mysql_db,mysql_port):
    return pymysql.connect(host=mysql_host,user=mysql_user,password = mysql_pw,port=mysql_port,db=mysql_db)
def get_table_info(table,mysql_host,mysql_user,mysql_pw,mysql_db,mysql_port,hive_db):
    '''
    :param table: mysql表名
    :param mysql_host: host
    :param mysql_user: 用户名
    :param mysql_pw: 密码
    :param mysql_db: db
    :param mysql_port: 端口(3306)
    :param hive_db: hive库
    :return: create_table_sql
    '''
    cols=[];
    create_head = "create table if not exists {0}.{0}_{1} (\n".format(hive_db,table)
    conn = get_mysql_conn(mysql_host,mysql_user,mysql_pw,mysql_db,mysql_port)
    try:
        with conn.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
            sql = "show full fields from {0}".format(table)
            count = cursor.execute(sql)
            try:
                for row in cursor:
                    if 'bigint' in row['Type']:
                        row['Type'] = "bigint"
                        cols.append('ifnull({0},"")'.format(row['Field']))
                    elif 'int' in row['Type'] or 'tinyint' in row['Type'] or 'smallint' in row['Type'] or 'mediumint' in row[
                        'Type'] or 'integer' in row['Type']:
                        row['Type'] = "int"
                        cols.append('ifnull({0},"")'.format(row['Field']))
                    elif 'double' in row['Type'] or 'float' in row['Type'] or 'decimal' in row['Type']:
                        row['Type'] = "double"
                        cols.append('ifnull({0},"")'.format(row['Field']))
                    else:
                        row['Type'] = "string"
                        cols.append('REPLACE( REPLACE( REPLACE( ifnull({0},""),"|", " "), "\\n", " "), "\\r", " ")'.format(row['Field']))
                    create_head +=row['Field']+' '+row['Type']+' comment \''+row['Comment']+'\''+',\n'
            except:
                print('异常')
    finally:
        conn.close()
    create_str = create_head[:-2] + '\n' + ')'+" ROW FORMAT DELIMITED FIELDS TERMINATED BY '{0}'".format('|')
    return cols, create_str

def get_mysql_data(table,mysql_host,mysql_user,mysql_pw,mysql_db,mysql_port,hive_db):
    conn = get_mysql_conn(mysql_host, mysql_user, mysql_pw, mysql_db, mysql_port)
    select_str = 'select CONCAT_WS("|",'
    cols, create_str = get_table_info('test_luzy_20190813', mysql_host, mysql_user, mysql_pw, mysql_db, mysql_port, hive_db)
    for col in cols:
        select_str += col +','
    select_str =select_str[:-1]+') as result from {0}.{1}'.format(mysql_db,table)
    result_file_name='C:\\tmp\\{0}.txt'.format(table)
    try:
        with conn.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
            count = cursor.execute(select_str)
            result = ''
            for rs in cursor:
                result=rs['result']
            with open(result_file_name,'w+') as result_file:
                result_file.write(result)
                put_hdfs_cmd = 'hdfs dfs -put {0} /tmp/datafolder'.format(result_file_name)
                # os.system(put_hdfs_cmd)
                load_data(create_str,table,hive_db)

    finally:
        conn.close()

def load_data(create_hive_table,table,hive_db):
    create_table_sql="hive -e '{0}'".format(create_hive_table)
    # os.system(create_table_sql)
    print(create_table_sql)
    load_data_sql = "hive -e 'load data inpath '/tmp/datafolder/{0}.txt' overwrite into table {1}.{2}'".format(table,hive_db,table)
    # os.system(load_data_sql)
    print(load_data_sql)

# main
if __name__ == '__main__':
    get_mysql_data('test_luzy_20190813', 'localhost', 'root', 'kobe24', 'test', 3306,'tmp')