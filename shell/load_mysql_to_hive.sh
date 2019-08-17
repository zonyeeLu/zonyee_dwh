#!/bin/bash
##########################################################
## 功能:mysql抽取数据到hive(自动建表)
## 参数 $1:mysql_host  $2:mysql_user $3:mysql_pw $4:mysql_port $5:mysql_table $6:mysql_db $7:hive_db
##########################################################
mysql_conn="mysql -h$1 -u$2 -p$3 -P$4"
#获取表信息
sql="show fields from $6.$5"
echo $sql|$mysql_conn |sed '1d'>./$5_fields.txt
#替换字符串
sed 's/\t/,/g' -i ./$5_fields.txt
#获取字段信息
hive_create_head="create table if not exists $7.$5( "
cols=''
while read line;do
  str=${line%?}
  arr=(${str//,/ })
  echo ${arr[0]} ${arr[1]}
  if [[ ${arr[1]} =~ 'double' ]] || [[ ${arr[1]} =~ 'float' ]] || [[ ${arr[1]} =~ 'decimal' ]]
  then
    echo "double"
    hive_create_head="${hive_create_head} ${arr[0]} double,"
    cols="${cols} ifnull(${arr[0]},''),"
  elif [[ ${arr[1]} =~ 'int' ]] || [[ ${arr[1]} =~ 'tinyint' ]] || [[ ${arr[1]} =~ 'smallint' ]] || [[ ${arr[1]} =~ 'mediumint' ]] || [[ ${arr[1]} =~ 'integer' ]] || [[ ${arr[1]} =~ 'bigint' ]]
  then
    echo "int"
    hive_create_head="${hive_create_head} ${arr[0]} bigint,"
    cols="${cols} ifnull(${arr[0]},''),"
  else
    echo "string"
    hive_create_head="${hive_create_head} ${arr[0]} string,"
    cols="${cols} REPLACE( REPLACE( REPLACE( ifnull(${arr[0]},''),'|', ' '), '\n', ' '), '\r', ' '),"
  fi
  echo ${hive_create_head}
done<./$5_fields.txt

# 拼接hive 建表语句
create_str="${hive_create_head:0:${#hive_create_head}-1} ) ROW FORMAT DELIMITED FIELDS TERMINATED BY '|'"
echo ${create_str}
#在hive上建表
#hvie -e "${create_str}"
#拼接mysql 查询语句
select_sql="select CONCAT_WS('|', ${cols:0:${#cols}-1} ) from $6.$5"
echo ${select_sql}|$mysql_conn |sed '1d'>/tmp/zonyee/$5_data.txt

#txt上传到hdfs
#hdfs dfs -put /tmp/zonyee/$5_data.txt /tmp/datafolder

#load数据进表
#hive -e "load data inpath '/tmp/datafolder/$5_data.txt' overwrite into table $7.$5"

# mysql -h10.0.11.181 -uroot -pkobe24 -P3306 -e "show fields from test.test_luzy_20190813"
# bash load_mysql_to_hive.sh 10.0.11.181 root kobe24 3306 test_luzy_20190813 test tmp
#mysql -h10.0.11.181 -uroot -pkobe24 -P3306 -N -e "select * from  test.test_luzy_20190813"
