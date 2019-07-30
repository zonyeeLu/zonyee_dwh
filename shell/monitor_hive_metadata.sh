#!/bin/bash
#mysql_conn=`cat "/tmp/zonyee/mysql_conn/mysql_conn.txt"`
mysql_conn='mysql -hlocalhost -P3306 -uroot -pkobe24'
echo $mysql_conn
#sql_str='select type_id,type_name from test.zonyee_test_20190723 into outfile "/tmp/zonyee/zonyee_txt_20190723.txt"'
sql_str='select type_id,type_name from test.zonyee_test_20190723'
echo $sql_str
$mysql_conn -e "$sql_str"
