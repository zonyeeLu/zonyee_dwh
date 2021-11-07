
### 并行度:一个MR程序中maptask和reducetask的任务量
#### Maptask的并行度决定机制(每个maptask处理一个逻辑切片)
    1. splitsize：blocksize,maxsize,minsize的中间值决定切片大小(min(blocksize,max(maxsize,minsize)))
    2. 不论如何调整参数,都不能将多个小文件划入一个split

 

### MapReduce的核心三大组件(在shuffle中起作用)
#### partitioner
     对maptask结果数据按照key值的某个值(如hash进行分区操作),并且设置reducetask分区
#### combiner
##### 1.定义:
      Combiner是mapreduce中Mapper和reducer之外的一个组件,作用于maptask之后对maptask的输出结果进行局部汇总,减轻reducetask的计算负载,减少网络传输
##### 2.使用: 
      Combiner与reducer是一样的,只是作用在maptask的节点
##### 3.Combiner与Reducer的区别
      1.combiner是在每一个maptask节点上运行,reducer是接受全局maptask的输出结果
      2.combiner的输出键值对与reducer接受的键值对保持一致
      3.Combiner 的使用要非常谨慎，因为 Combiner 在 MapReduce 过程中可能调用也可能不调 用，可能调一次也可能调多次，所以： Combiner 使用的原则是：有或没有都不能影响业务 逻辑，都不能影响最终结果(求平均值时，combiner和reduce逻辑不一样)
#### sorter
     如果需要对key值进行排序时,可以直接排序; 但是当需要对value中某个字段排序时,将字段提升到key中,重新实现sort方法进行排序

### MapJoin 和 ReduceJoin 
#### 1.ReduceJoin(common join)
     如果不指定MapJoin或者不符合MapJoin的条件,那么hive会解析器会将join操作转化成common join (在reduce 中完成reduce完成join)
     Map阶段
     读取源表的数据，Map输出时候以Join on条件中的列为key，如果Join有多个关联键，则以些关联键的组合作为key;
     Map输出的value为join之后所关心的(select或者where中需要用到的)列；同时在value中会包含表的Tag信息，用于标明此value对应哪个表；
     按照key进行排序

     Shuffle阶段
     根据key的值进行hash,并将key/value按照hash值推送至不同的reduce中，这样确保两个中相同的key位于同一个reduce中

     Reduce阶段
     根据key的值完成join操作，期间通过Tag来识别不同表中的数据。
     对接收到的kv对,分别将不同数据标识的value写入不同的list中,例如关联的表存在两个,则有两个list,
     做一个笛卡尔积(两个for循环)分别遍历两个list,将同一个key的两个list拼接在一起
#### 2.MapJoin
     MapJoin通常用于小表跟大表进行join操作的场景,由以下参数进行控制(因为每一个maptask只能处理一个逻辑切块,所以将其放入内存中,不需要maptask进行处理)
     (1) hive.mapjoin.smalltable.filesize=25000000(默认25M)
     (2) hive.auto.convert.join=true(开启mapjoin)
     流程(针对两个表join):
     启用一个local task(不是maptask)负责扫描小表,将其转换成一个HashTable的数据结构,并将其写入本地文件中,之后将其加载到DistributeCache中 (底层代码初始化,利用mapper的setup方法)
     启用Maptask扫描大表,在map阶段,根据大表的每一条记录在DistributeCache 中找相同的key,并且直接输出结果(不需要reduce)
     由于mapjoin没有reduce阶段,所以maptask的数量就是输出文件的数量
#### 3.当两者都为大表时的数据处理方案
     1. 按照连接条件的hash值将表分区
     2. hive中作分区表(hive中底层自动优化,如果优化效果不够则需要手动优化)