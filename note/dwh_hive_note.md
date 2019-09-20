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
    
          
     
    
         
        
    