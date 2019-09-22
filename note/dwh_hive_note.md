#Hive大概了解  

####1.什么是hive   

    (1) hive是基于hadoop的一个数据仓库  
    (2) hive可以将结构化的数据映射为一张数据库表  
    (3) hive底层的数据在hdfs上,并且提供了hive sql查询(hql最终是转化为mapreduce执行的)  
    
####2.hive 的特点  

    (1)优点  
        1)扩展性横向拓展  
        2)延展性:hive支持自定义函数(udf udaf udtf)  
        3)良好的容错性  
    (2)缺点  
        1)hive不支持记录级别的update操作  
        2)hive查询延迟很严重  
        3)hive不支持事务  
      
####3.hive sql  

    此部分主要是sql语法,平时工作中积累即可  
    
####4.hive元数据  

    (1)hive元数据就是存储hive库信息,表信息,字段信息,文件格式信息等等,通常是mysql  
    (2)DBS:存放hive中数据库的信息  
    (3)TBLS:存放表信息  
    (4)SDS:存放文件存储的信息  
    (5)COLUMNS_V2:存放字段信息  
    (6)完整信息可以查看: http://note.youdao.com/noteshare?id=a8e85553c7262081a7c47b7d68d5bfee&sub=F93DAC1182394D74B6B8C2A43DED2FE6  
    
####5.hive文件格式以及压缩效率  

    (1) 行存储和列存储  
        1)行存储  
          1. 相关的数据存在一起,一行就是一条记录  
          2. 方便进行insert 和update  
          3. 数据读取的时候会把整行读取出来  
        2)列存储  
          1.数据读取时可以跳过不必要查询的列  
          2.高效压缩率  
          3.任何列都可以作为索引  
          4.insert/update不方便  
          5.不适合扫描小数据量  
    (2) TextFile  
        默认格式,不支持压缩,磁盘开销大,数据解析开销大  
    (3) RCFile  
        行列存储相结合,先将数据按行分块,保证同一条记录在一个块上,避免读一个记录要读取多个块  
        数据块按照列存储,有利于数据压缩和快速的存取  
    (4) ORCFile  
        是RCFile优化版  
    (5) parquet  
        列存储,能够很好的压缩,查询性能良好  
    (6) Sequencefile 二进制编码,数据压缩 无法可视化 行存储  以<key,value>的形式序列化到文件中  
    (7) 压缩效率: ORCFile(50倍) > parquet(10倍) > RCFile(1.5倍) > Sequencefile(1.3倍) > TextFile  
    (8) 查询效率: ORCFile > parquet > RCFile > Sequencefile > TextFile  
    
####6.hive分区分桶  

    (1)分区  
       1.在表目录下创建文件目录,是一个伪列(不是表中的某一列)  
       2.避免全表扫描,提高查询效率  
       3.单值分区(直接定义分区列或者create table like,注意不能create table as select 创建分区表)    
         (1)静态分区  
         (2)动态分区 set hive.exec.dynamic.partition=true/set hive.exec.max.dynamic.partitions=2000  
       4.范围分区(只能通过直接定义分区列创建范围分区表.分区键前闭后开,最后出现的分区可以使用 MAXVALUE 作为上限MAXVALUE 代表该分区键的数据类型所允许的最大值)  
         (1)DROP TABLE IF EXISTS test_demo;  
            CREATE TABLE test_demo (value INT)  
            PARTITIONED BY RANGE (id1 INT, id2 INT, id3 INT) 
            (  
                -- id1在(--∞,5]之间，id2在(-∞,105]之间，id3在(-∞,205]之间  
                PARTITION p5_105_205 VALUES LESS THAN (5, 105, 205),  
                -- id1在(--∞,5]之间，id2在(-∞,105]之间，id3在(205,215]之间  
                PARTITION p5_105_215 VALUES LESS THAN (5, 105, 215),  
                PARTITION p5_115_max VALUES LESS THAN (5, 115, MAXVALUE),  
                PARTITION p10_115_205 VALUES LESS THAN (10, 115, 205),  
                PARTITION p10_115_215 VALUES LESS THAN (10, 115, 215),  
                PARTITION pall_max values less than (MAXVALUE, MAXVALUE, MAXVALUE)  
            );  

    (2)分桶  
       1.将表中记录按照分桶键(表中的某一列)的哈希值分散进入多个文件中  
       2.创建方式:  
         (1)直接建表 CLUSTERED BY(pcid) INTO 10 BUCKETS 
            sorted by (uid desc) – 指定数据的排序规则，表示预期的数据就是以这里设置的字段以及排序规则来进行存储   
         (2)create table like  
         (3)create table as select(单值分区不能这样使用)  
       3.写入数据方式:  
         (1) SET hive.enforce.bucketing=true;  
         (2) 将reducer个数设置为目标表的桶数，并在 SELECT 语句中用 DISTRIBUTE BY <bucket_key>对查询结果按目标表的分桶键分进reducer中  
             SET mapred.reduce.tasks = <num_buckets>  
             DISTRIBUTE BY <bucket_key> 
       4.取值方式  
         tablesample(bucket x out of y on uid)  
         x:代表从第几桶开始查询  
         y:查询的总桶数,y可以是总的桶数的倍数或者因子;x不能大于y  
         total_bucket/y: 大于1表示取几个桶的数据(x/(x+y)...)  
                         小于1表示取第x个桶的total_bucket/y数据  
                         
####6.hive调优
                     
         
           
         
     
    
         
        
    