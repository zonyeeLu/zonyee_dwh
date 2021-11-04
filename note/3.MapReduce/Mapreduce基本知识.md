
### 并行度:一个MR程序中maptask和reducetask的任务量
#### Maptask的并行度决定机制(每个maptask处理一个逻辑切片)
    1. splitsize：blocksize,maxsize,minsize的中间值决定切片大小(min(blocksize,max(maxsize,minsize)))
    2. 不论如何调整参数,都不能将多个小文件划入一个split

#### Reducetask的并行度决定机制(一个reducetask往外输出一个结果文件)
    1. MR程序当中的reducetask的个数默认为1
    2. reducetask的数量可以随意设置,当设置为0时,输出结果为map的输出(默认情况)
    在特定情况下,不能随意设置,如全局统计求和,只能用一个reducetask

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