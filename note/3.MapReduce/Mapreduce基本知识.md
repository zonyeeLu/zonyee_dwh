
### 并行度:一个MR程序中maptask和reducetask的任务量
#### Maptask的并行度决定机制(每个maptask处理一个逻辑切片)
    1. splitsize：blocksize,maxsize,minsize的中间值决定切片大小(min(blocksize,max(maxsize,minsize)))
    2. 不论如何调整参数,都不能将多个小文件划入一个split

#### Reducetask的并行度决定机制(一个reducetask往外输出一个结果文件)
    1. MR程序当中的reducetask的个数默认为1
    2. reducetask的数量可以随意设置,当设置为0时,输出结果为map的输出(默认情况)
    在特定情况下,不能随意设置,如全局统计求和,只能用一个reducetask

### MapReduce的核心三大组件
#### partitioner
     
#### combiner
#### sorter