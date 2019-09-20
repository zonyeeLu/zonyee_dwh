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
    (1)
     
    
         
        
    