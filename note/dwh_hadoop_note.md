#Hadoop 框架的大概了解  

####1.什么是hadoop  
    (1) hadoop 还分布式系统基础架构,解决了大数据的可靠存储和处理(hdfs/mapreduce)
    (2) hadoop 的两大功能:海量数据的存储 海量数据的分析
    (3) hadoop 的三大核心组件:
        1.Hdfs:分布式文件系统
        2.MapReduce: 计算框架
        3.Yarn:集群资源调度系统 
    (4) https://www.processon.com/view/link/5d80a304e4b04c14c4e6522a
    
####2.分布式文件系统(Hdfs)能够存储海量数据的原理  
    (1) 元数据和数据  
        1.元数据:文件名,文件权限,数据块位置,副本数等等
        2.数据:存放文件的实际内容  
    (2) HDFS是拿出一台或者多台机器来保存元数据,其他机器保存文件数据
        其中两个核心: NameNode:存放元数据(master)
                     DataNode:存放文件数据(slave)  
    (3)Hdfs的写过程  
       1.client 向NameNode发送请求,NameNode检查文件是否存在,父路径是否存在(路径不存在会报错)  
       2.NameNode 向client 反馈是否可以上传  
       3.client 对文件进行切分(128M)成block,请求第一个block发送到那些DataNode上  
       4.NameNode返回可以存放数据的DataNode   
       5.client请求最近的一台DataNode上传数据(socket连接),第一台DataNode请求调用第二台,一次类推并且建立pipeline  
         然后返回client,注意client只会与第一台DataNode建立连接  
       6.client开始传输block(先从本地磁盘读取数据到一个本地内存缓存),packet为单位(64kb),写入数据到datanode的时候  
         会进行数据校验(chunk 512b),client每向DataNode写入一个packet,都会直接把这个packet从pipeline中传给其他DataNode    
         (并不是写好一个块或一整个文件后才向后分发)  
       7.写完数据关闭输出流
       8.DataNode发送信息给NameNode(发送完成信号的时机取决于集群是强一致性还是最终一致性,强一致性则需要所有DataNode写完后才向NameNode汇报.最终一致性则其中任意一个DataNode写完后就能单独向NameNode汇报,HDFS一般情况下都是强调强一致性)    
       9.如果再pipeline传输中,任意节点失败,上游节点直接连接失败节点的下游节点继续传输,最终在第5步汇报后,NameNode会发现副本数不足,一定会出发DataNode复制更多副本,客户端Client副本透明  
       10.client 与NameNode 是通过rpc通信   
          DataNode 与NameNode是通过rpc通信  
          client与DataNode通过socket通信  
          
    (4)Hdfs的读过程  