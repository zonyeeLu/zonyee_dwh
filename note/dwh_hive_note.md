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

    (1) mapreduce不担心处理大数据,而是担心数据倾斜,慎用count(distinct)  
    (2) 设置合理的map数和reduce数  
        1.map阶段:  
          (1)减少map数:  
             当表文件是很多个远小于128m的文件时(100个,共10g),正常情况下会启动100个map去执行  
             此时可以调整参数:  
             set mapred.max.split.size=100000000;  
             set mapred.min.split.size.per.node=100000000;  
             set mapred.min.split.size.per.rack=100000000;  
             set hive.input.format=org.apache.hadoop.hive.ql.io.CombineHiveInputFormat;    
             100000000是100m,文件大小大于128m,则按照128来切分;100-128则按照100m切分;小于100m则合并  
             从而减少了map数  
          (2)增加map数:  
             当表(table_a)文件只有一个文件时,并且只有两个字段,文件大小1g  
             可以将table_a写入table_b并且设置set mapred.reduce.tasks=10;从而拆成10个小文件  
             从而增大了map数  
          综上:使用单个map处理合适的数据量  
        2.reduce阶段:  
          (1) reduce个数对整个作业的运行影响很大,reduce个数过大会产生很多小文件从而影响NameNode  
              reduce个数过少那么单个reduce处理的数据就会加大可能会引起内存溢出  
              mapred.reduce.tasks/mapreduce.job.reduces hive会直接使用他们的值作为reduce个数  
          (2) hive.exec.reducers.bytes.per.reducer 每个reduce默认处理数据的数量是1g  
              hive.exec.reducers.max 每个任务最大的reduce个数默认是999  
          (3) 只有一个reduce的情况  
              1.没有group by 的汇总  select count(1) from popt_tbaccountcopy_mes where pt = ‘2012-07-04’  
              2.用了order by  
              3.产生了笛卡尔积  
          (4) 小文件的合并  是否合并Map输出文件:hive.merge.mapfiles=true(默认值为真)/合并Reduce 端输出文件hive.merge.mapredfiles=false(默认值为假)/合并文件的大小:hive.merge.size.per.task=256*1000*1000(默认值为 256000000)  
              1.产生小文件的原因:  
                (1)动态分区插入数据,分区字段的key很多  
                (2)reduce数量很多  
                (3)数据源本身就包含很多小文件  
              2.小文件的影响  
                (1)每个小文件都要启动一个map去执行,map的启动初始化都会浪费大量的资源  
                (2)小文件都占用大量的元数据内存,会对NameNode造成影响  
              3.小文件问题的解决方案  
                (1)少使用动态分区或者动态分区字段需要慎重选择  
                (2)控制reduce个数  
                (3)使用压缩文件存储,并且进行文件合并  
                (4)对已存在大量的小文件,可以重建表控制reduce个数  
        3.Map join  
          (1) 通过mapreduce local task 将小表(1g)读入到内存中生成hashtablefile上传到distributed cache 中  
          (2) 在map阶段,每个mapper从distributed cache读取hashtablefile到内存中顺序扫描大表,在map阶段进行join将数据传给下个mapreduce任务  
              也就是在map端进行join避免了shuffle  
        4.引擎选择  
          hive.execution.engine = tez  
        5.sql语法的优化  
          1.通过子查询先把不用的数据过滤掉  
          2.用distinct和union all 代替 union  
          3.数据倾斜处理  
            (1)过滤掉倾斜的key(如null)  
            (2)打散倾斜的key(加随机值)  
            (3)数据倾斜参数调整 hive.map.aggr = true 在map端做聚合 combiner (相当于是本地的reduce 并不适用avg)  
                              hive.groupby.skewindata = true 是负载均衡 但是支持是一个count(distinct)  
                              原理:启动两个mr 第一个将map数据随机分配到reducer中 做部分聚合操作 这样处理是相同的key可能在不同的reducer中  
                                  第二个mr 根据group by key 相同的key分配到同一个reduce中 因为第一个mr已经经过预计算  
          4.避免一个sql中包含负责的处理逻辑,可以使用中间表  
          5.当对不同的表时:如果union all的部分个数大于2,或者每个union部分数据量大,应该拆成多个insert into 语句,实际测试过程中,执行时间能提升50%  
            当对同一张表: union all 效率比insert into 要高  
         
        
                
        
             
             
    
                     
         
           
         
     
    
         
        
    