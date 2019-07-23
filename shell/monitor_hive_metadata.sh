#!/bin/bash
mysql_conn=`cat "/tmp/zonyee/mysql_conn/mysql_conn.txt"`
echo $mysql_conn
sql_str='select type_id,type_name from test.zonyee_test_20190723 into outfile "/tmp/zonyee/zonyee_txt_20190723.txt"'
echo $sql_str
echo $sql_str|$mysql_conn
